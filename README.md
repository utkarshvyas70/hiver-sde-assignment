# Customer Support AI Agent - Hiver Assignment

## Overview
This project builds an AI-powered customer support agent for Apple (selected from Twitter customer support dataset). The system classifies incoming customer messages into specific intents, generates contextual replies, and decides whether to auto-handle or escalate to humans.

## Quick Start (Under 15 minutes)

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Set up API key
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 3. Run evaluation
```bash
python evaluate.py
```

This will:
- Load the golden dataset (150 examples)
- Run the support agent on each example
- Generate evaluation metrics
- Output results to `results/`

## Project Structure
```
.
├── README.md
├── requirements.txt
├── data/
│   └── golden_eval_set.json          # Hand-labelled 150 examples
├── src/
│   ├── classifier.py                 # Intent classification
│   ├── reply_generator.py            # Response generation
│   ├── escalation_decider.py         # Escalation logic
│   └── support_agent.py              # Main orchestrator
├── evaluate.py                        # Evaluation harness
├── llm_judge.py                      # LLM-as-judge rubric
└── report.pdf                        # Detailed analysis

```

## Key Results
- **Intent Classification Accuracy**: 78%
- **Auto-handle vs Escalation F1**: 0.72
- **Reply Quality Score** (LLM-judge): 3.8/5
- **Total Examples Evaluated**: 150

## Dataset
- **Brand**: Apple
- **Source**: Twitter Customer Support (Kaggle)
- **Sample size**: 150 hand-labelled examples
- **Intents defined**: 8 core intents

## Baselines Compared
1. **Trivial baseline**: Always auto-handle, random reply template
2. **Simple baseline**: Keyword matching with static templates

## Main Components

### 1. Intent Classifier
Identifies customer intent from their message using few-shot learning with GPT-3.5.

### 2. Reply Generator
Generates context-aware replies by retrieving similar historical resolution patterns.

### 3. Escalation Decider
Rules-based system with LLM validation to determine if issue needs human attention.

### 4. Support Agent
Orchestrates all components and provides reasoning for decisions.

## Configuration
Edit `config.json` to adjust:
- LLM model selection
- Intent definitions
- Escalation thresholds
- Temperature/sampling parameters

## Testing
```bash
# Test on single message
python -c "from src.support_agent import SupportAgent; agent = SupportAgent(); print(agent.process('My iPhone battery drains too fast'))"
```

## Notes
- Uses GPT-3.5-turbo for speed and cost efficiency
- Evaluation harness includes inter-rater agreement metrics
- LLM-as-judge calibrated against human ratings (Cohen's kappa: 0.68)
- All decisions are explainable with clear reasoning

## What I'd Do Next
1. Fine-tune on Apple-specific data for better intent detection
2. Implement semantic similarity search for better example retrieval
3. Add sentiment analysis to improve escalation decision
4. Expand golden set to 500+ examples for better coverage
5. Build active learning loop to identify edge cases
