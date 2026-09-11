import json
import os
from collections import defaultdict
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from src.support_agent import SupportAgent

def load_golden_set():
    with open('data/golden_eval_set.json', 'r') as f:
        return json.load(f)

def trivial_baseline(message):
    return {
        "intent": "feature_question",
        "reply": "Thank you for reaching out to Apple support. How can I help you today?",
        "should_escalate": False,
        "escalation_reason": "Trivial baseline auto-handles everything"
    }

def keyword_baseline(message):
    keywords_intent = {
        "battery": "device_issue",
        "update": "software_update",
        "password": "account_access",
        "warranty": "warranty_question",
        "order": "order_tracking",
        "charged": "billing_issue",
        "how": "feature_question",
        "thank": "compliment",
        "broke": "device_issue"
    }
    
    intent = "feature_question"
    for keyword, detected_intent in keywords_intent.items():
        if keyword in message.lower():
            intent = detected_intent
            break
    
    template_replies = {
        "device_issue": "Try restarting your device first. If that doesn't work, backup and restore.",
        "billing_issue": "Check your account settings for subscription details.",
        "software_update": "Updates are in Settings > General > Software Update.",
        "account_access": "Use iforgot.apple.com to reset your password.",
        "warranty_question": "Standard warranty is 1 year. Check apple.com/support for details.",
        "feature_question": "Check support.apple.com for guides and tutorials.",
        "order_tracking": "Check your order status at apple.com in your account.",
        "compliment": "Thank you for your feedback!"
    }
    
    escalate = any(word in message.lower() for word in ["angry", "lawyer", "lawsuit", "urgent"])
    
    return {
        "intent": intent,
        "reply": template_replies[intent],
        "should_escalate": escalate,
        "escalation_reason": "Keyword match" if escalate else "Auto-handle"
    }

def evaluate_agent(agent, golden_set):
    examples = golden_set["examples"]
    
    predictions = []
    for example in examples:
        result = agent.process(example["message"])
        predictions.append({
            "id": example["id"],
            "predicted_intent": result["intent"],
            "true_intent": example["intent"],
            "predicted_escalate": result["should_escalate"],
            "true_escalate": example["should_escalate"],
            "reply": result["reply"]
        })
    
    true_intents = [ex["intent"] for ex in examples]
    pred_intents = [p["predicted_intent"] for p in predictions]
    
    intent_accuracy = accuracy_score(true_intents, pred_intents)
    
    true_escalate = [ex["should_escalate"] for ex in examples]
    pred_escalate = [p["predicted_escalate"] for p in predictions]
    escalate_accuracy = accuracy_score(true_escalate, pred_escalate)
    
    precision, recall, f1, _ = precision_recall_fscore_support(
        true_escalate, pred_escalate, average='binary'
    )
    
    return {
        "predictions": predictions,
        "metrics": {
            "intent_accuracy": intent_accuracy,
            "escalation_accuracy": escalate_accuracy,
            "escalation_precision": precision,
            "escalation_recall": recall,
            "escalation_f1": f1,
            "total_examples": len(examples)
        }
    }

def create_baselines_comparison(golden_set):
    examples = golden_set["examples"]
    
    trivial_results = {"correct_intent": 0, "correct_escalate": 0}
    keyword_results = {"correct_intent": 0, "correct_escalate": 0}
    
    for example in examples:
        trivial = trivial_baseline(example["message"])
        keyword = keyword_baseline(example["message"])
        
        if trivial["intent"] == example["intent"]:
            trivial_results["correct_intent"] += 1
        if trivial["should_escalate"] == example["should_escalate"]:
            trivial_results["correct_escalate"] += 1
        
        if keyword["intent"] == example["intent"]:
            keyword_results["correct_intent"] += 1
        if keyword["should_escalate"] == example["should_escalate"]:
            keyword_results["correct_escalate"] += 1
    
    total = len(examples)
    
    return {
        "trivial_baseline": {
            "intent_accuracy": trivial_results["correct_intent"] / total,
            "escalation_accuracy": trivial_results["correct_escalate"] / total,
            "description": "Random intent assignment, auto-handle all"
        },
        "keyword_baseline": {
            "intent_accuracy": keyword_results["correct_intent"] / total,
            "escalation_accuracy": keyword_results["correct_escalate"] / total,
            "description": "Simple keyword matching with template responses"
        }
    }

def print_results(agent_results, baselines):
    print("\n" + "="*60)
    print("CUSTOMER SUPPORT AI AGENT - EVALUATION RESULTS")
    print("="*60)
    
    metrics = agent_results["metrics"]
    print(f"\n📊 PRIMARY AGENT METRICS (n={metrics['total_examples']})")
    print(f"   Intent Classification Accuracy:  {metrics['intent_accuracy']:.1%}")
    print(f"   Escalation Accuracy:             {metrics['escalation_accuracy']:.1%}")
    print(f"   Escalation Precision:            {metrics['escalation_precision']:.2f}")
    print(f"   Escalation Recall:               {metrics['escalation_recall']:.2f}")
    print(f"   Escalation F1 Score:             {metrics['escalation_f1']:.2f}")
    
    print(f"\n🔸 BASELINE COMPARISON")
    print(f"   Trivial Baseline (Random):")
    print(f"      Intent Accuracy:  {baselines['trivial_baseline']['intent_accuracy']:.1%}")
    print(f"      Escalation Acc:   {baselines['trivial_baseline']['escalation_accuracy']:.1%}")
    
    print(f"   Keyword Baseline:")
    print(f"      Intent Accuracy:  {baselines['keyword_baseline']['intent_accuracy']:.1%}")
    print(f"      Escalation Acc:   {baselines['keyword_baseline']['escalation_accuracy']:.1%}")
    
    improvement = (metrics['intent_accuracy'] - baselines['keyword_baseline']['intent_accuracy']) * 100
    print(f"\n📈 IMPROVEMENT: +{improvement:.1f} points vs keyword baseline")
    
    print("\n✅ Sample Correct Predictions:")
    correct = [p for p in agent_results["predictions"] if p["predicted_intent"] == p["true_intent"] and p["predicted_escalate"] == p["true_escalate"]]
    for pred in correct[:3]:
        print(f"   Example {pred['id']}: {pred['predicted_intent'].replace('_', ' ').title()}")
    
    print("\n❌ Top Misclassifications:")
    incorrect = [p for p in agent_results["predictions"] if p["predicted_intent"] != p["true_intent"]]
    for pred in incorrect[:3]:
        print(f"   Expected: {pred['true_intent'].replace('_', ' ').title()}")
        print(f"   Got:      {pred['predicted_intent'].replace('_', ' ').title()}")
    
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    print("Loading golden evaluation set...")
    golden_set = load_golden_set()
    
    print("Initializing support agent...")
    agent = SupportAgent()
    
    print("Evaluating agent...")
    agent_results = evaluate_agent(agent, golden_set)
    
    print("Computing baseline comparisons...")
    baselines = create_baselines_comparison(golden_set)
    
    print_results(agent_results, baselines)
    
    os.makedirs('results', exist_ok=True)
    with open('results/evaluation_results.json', 'w') as f:
        json.dump({
            "agent_results": agent_results,
            "baselines": baselines
        }, f, indent=2)
    
    print("Results saved to results/evaluation_results.json")
