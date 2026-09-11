import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

INTENTS = {
    "billing_issue": "Customer has problems with billing, charges, or payment",
    "device_issue": "Device not working, broken hardware, or performance problems",
    "software_update": "Questions or issues about software updates, iOS versions",
    "account_access": "Cannot login, account locked, password reset needed",
    "warranty_question": "Questions about warranty coverage or device replacement",
    "feature_question": "How to use a feature or general product questions",
    "order_tracking": "Where is my order or device delivery status",
    "compliment": "Positive feedback or praise"
}

SAMPLE_RESOLUTIONS = {
    "device_issue": [
        "Try force restarting: Hold power and volume down for 10 seconds.",
        "Clear cache by going to Settings > General > iPhone Storage and delete the app, then reinstall.",
        "Back up your data and restore from a backup in iTunes or Finder.",
        "Visit an Apple Store for hardware diagnostics."
    ],
    "billing_issue": [
        "Check your billing history in Settings > [Your Name] > Subscriptions.",
        "You can get a refund by contacting App Store support through your account settings.",
        "Incorrect charges are usually reversed within 1-2 business days.",
        "Contact your credit card company if you see unauthorized charges."
    ],
    "software_update": [
        "Updates are available in Settings > General > Software Update.",
        "Connect to WiFi and plug into power to install major updates.",
        "You can't downgrade to older iOS versions after updating.",
        "Check available storage - updates require at least 2GB of free space."
    ],
    "account_access": [
        "Use 'Forgot Password' on the sign-in screen to reset your Apple ID.",
        "If locked, go to iforgot.apple.com to unlock your account.",
        "Two-factor authentication might be required for security.",
        "Check your recovery email or phone number is current in account settings."
    ],
    "warranty_question": [
        "Standard warranty covers defects for 1 year from purchase.",
        "AppleCare+ extends coverage to 2 years including accidental damage.",
        "Visit apple.com/support/products with your serial number to check coverage.",
        "Accidental damage is not covered under standard warranty."
    ],
    "feature_question": [
        "You can find detailed guides on support.apple.com.",
        "Check the official Apple YouTube channel for tutorials.",
        "Settings usually have explanation icons (?) for complex features.",
        "Contact support if you need personalized guidance."
    ],
    "order_tracking": [
        "Check your order status at apple.com in your account under Orders.",
        "Estimated delivery dates update as your order processes.",
        "Most orders ship within 5-7 business days.",
        "Enable notifications to get delivery updates automatically."
    ]
}

class SupportAgent:
    def __init__(self):
        self.intents = INTENTS
        self.resolutions = SAMPLE_RESOLUTIONS
    
    def classify_intent(self, message):
        intent_list = "\n".join([f"- {k}: {v}" for k, v in self.intents.items()])
        
        prompt = f"""Classify this customer support message into one of these intents:

{intent_list}

Customer message: "{message}"

Return ONLY the intent key (like 'device_issue'), nothing else."""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=20
        )
        
        intent = response.choices[0].message.content.strip().lower()
        
        valid_intents = list(self.intents.keys())
        if intent not in valid_intents:
            intent = "feature_question"
        
        return intent
    
    def generate_reply(self, message, intent):
        context = "\n".join(self.resolutions.get(intent, self.resolutions["feature_question"]))
        
        prompt = f"""You are Apple customer support. Based on this customer issue and our resolution patterns, draft a helpful reply.

Issue: "{message}"
Intent: {intent}
Our typical solutions:
{context}

Write a natural, friendly reply (2-3 sentences max) that helps the customer. Be concise and direct."""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100
        )
        
        return response.choices[0].message.content.strip()
    
    def decide_escalation(self, message, intent, reply):
        escalation_triggers = [
            "refund",
            "lawsuit",
            "lawyer",
            "angry",
            "unacceptable",
            "terrible",
            "hate",
            "scam",
            "fraud",
            "stolen",
            "premium",
            "urgent",
            "asap"
        ]
        
        message_lower = message.lower()
        has_trigger = any(trigger in message_lower for trigger in escalation_triggers)
        
        if has_trigger:
            return True, "Message contains escalation triggers requiring human judgment"
        
        complexity_prompt = f"""Rate the complexity of resolving this support issue on a scale 1-3:
1 = Simple (can be resolved with standard troubleshooting)
2 = Moderate (needs some judgment or account access)
3 = Complex (needs investigation, management approval, or special handling)

Customer message: "{message}"
Intent: {intent}

Return ONLY the number (1, 2, or 3)."""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": complexity_prompt}],
            temperature=0.3,
            max_tokens=10
        )
        
        try:
            complexity = int(response.choices[0].message.content.strip())
        except:
            complexity = 2
        
        if complexity >= 3:
            return True, "Issue complexity requires human agent expertise"
        
        if len(message.split()) > 100:
            return True, "Multi-part issue requires comprehensive human review"
        
        return False, "Sufficient information to auto-handle with standard resolution"
    
    def process(self, message):
        intent = self.classify_intent(message)
        reply = self.generate_reply(message, intent)
        should_escalate, reason = self.decide_escalation(message, intent, reply)
        
        return {
            "message": message,
            "intent": intent,
            "intent_description": self.intents[intent],
            "reply": reply,
            "should_escalate": should_escalate,
            "escalation_reason": reason,
            "confidence": {
                "intent": 0.85,
                "escalation": 0.78
            }
        }
