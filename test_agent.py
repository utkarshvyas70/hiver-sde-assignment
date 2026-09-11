import os
from src.support_agent import SupportAgent

test_messages = [
    "My iPhone battery drains too fast, what should I do?",
    "I was charged twice for my subscription and I'm furious!",
    "How do I update to iOS 17?",
    "My Apple ID was hacked, please help immediately!",
    "Just got my new MacBook and it's amazing!",
    "My order hasn't arrived in 2 weeks",
    "Does AppleCare+ cover water damage?",
    "Can't login to my account, forgot password"
]

def test_agent():
    print("Initializing support agent...")
    agent = SupportAgent()
    
    print("\nTesting on 8 sample messages:\n")
    print("="*70)
    
    for i, message in enumerate(test_messages, 1):
        result = agent.process(message)
        
        print(f"\n[Example {i}]")
        print(f"Customer: {message}")
        print(f"Intent: {result['intent'].replace('_', ' ').title()}")
        print(f"Reply: {result['reply']}")
        print(f"Escalate: {result['should_escalate']}")
        print(f"Reason: {result['escalation_reason']}")
        print("-"*70)

if __name__ == "__main__":
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not set!")
        print("Run: export OPENAI_API_KEY='your-key-here'")
        exit(1)
    
    test_agent()
