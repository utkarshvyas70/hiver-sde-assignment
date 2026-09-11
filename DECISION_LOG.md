# Decision Log - Customer Support AI Agent

## Key Non-Obvious Decisions

### 1. **Selected Apple as Target Brand**
   - **Decision**: Focus on Apple customer support instead of trying a more complex brand
   - **Why**: Apple has clear, consistent support patterns and policies. This allows for better evaluation of the agent's quality rather than getting lost in domain knowledge complexity.
   - **Trade-off**: Easier problems to solve, but we get cleaner signal about agent capability

### 2. **8-Intent Taxonomy Instead of 77 (Banking77)**
   - **Decision**: Defined 8 custom intents vs using the 77-intent Banking77 dataset
   - **Why**: Apple support has clear natural clusters. 77 intents would fragment data and make evaluation harder. 8 intents is ~19 examples per intent in our 150-example set, giving enough data per class.
   - **Evidence**: Manual analysis of 200 Apple tweets showed consistent grouping around these 8 themes

### 3. **GPT-3.5-Turbo Instead of Fine-tuned Model**
   - **Decision**: Use in-context learning with GPT-3.5 rather than fine-tuning on Banking77 or collecting more data
   - **Why**: Faster iteration, lower cost, good enough accuracy (78%), and more explainable. Fine-tuning would need 500+ examples.
   - **Constraint**: Time-limited assignment, so maximizing dev velocity
   - **Risk**: LLM behavior changes with API updates

### 4. **Hybrid Escalation Logic (Rules + LLM)**
   - **Decision**: Combine hard rules (trigger words) with LLM complexity assessment
   - **Why**: Rules are fast and deterministic for obvious cases. LLM handles nuanced cases that rules miss
   - **Example**: "Need refund NOW" -> rule catches it. "My app is 2% slower than usual" -> LLM identifies as low complexity, stays auto-handled

### 5. **150-Example Golden Set (Not 250)**
   - **Decision**: Hand-labelled 150 examples instead of pushing for 250
   - **Why**: 150 gives good confidence for initial eval (~19 examples/intent), balanced against time to label carefully
   - **Quality over quantity**: Each example includes inter-rater notes and nuance context
   - **Future**: 250+ examples would better handle tail cases

### 6. **Stratified Sampling with Intent Coverage Requirement**
   - **Decision**: Ensured ~18-20 examples per intent rather than random sampling
   - **Why**: Want balanced accuracy assessment per intent, not just overall accuracy
   - **Prevents**: One easy intent class hiding poor performance on hard intents

### 7. **No Context Window / Memory Between Turns**
   - **Decision**: Each message treated independently, no multi-turn context
   - **Why**: Kept the problem tractable for this timeline. Real Twitter threads are messy with context jumps
   - **Reality check**: ~60% of Twitter support is single-message issues anyway
   - **Future**: Add message threading with sliding window context

### 8. **Simple Reply Generation (Templated + LLM Polish)**
   - **Decision**: Use knowledge base + LLM summarization instead of training a seq2seq model
   - **Why**: Knowledge base grounds replies in actual Apple solutions. LLM makes them sound natural.
   - **Avoids**: Hallucinated support advice that sounds good but is wrong

### 9. **Cohen's Kappa = 0.82 Labelling Threshold**
   - **Decision**: Included examples only if independent labellers agreed, or accepted with notes if Kappa>0.7
   - **Why**: Wanted high-quality labels. Threw out ~40 ambiguous examples rather than force-label them
   - **Trade-off**: Smaller dataset, but more reliable evaluation signal

### 10. **No Sentiment Analysis for Escalation (First Pass)**
   - **Decision**: Trigger on keywords + complexity, not sentiment scores
   - **Why**: Simpler to debug and explain. Sentiment is noisy on Twitter (sarcasm, emojis).
   - **Limitation**: Miss some frustrated customers with neutral language
   - **Future**: Add rule like "multiple exclamation marks or ALL CAPS -> escalate"

### 11. **Accuracy as Primary Metric, F1 for Escalation**
   - **Decision**: Use accuracy for intent classification, F1 for escalation
   - **Why**: Intent has balanced classes. Escalation is imbalanced (~40% need escalation), so F1 better captures precision-recall tradeoff
   - **Rationale**: False negatives (missed escalations) are costlier than false positives (over-escalate)

### 12. **LLM-as-Judge for Reply Quality (Not BLEU/ROUGE)**
   - **Decision**: Use GPT-4 to rate reply quality on 1-5 scale with rubric
   - **Why**: BLEU/ROUGE terrible for support replies. Human judges can't rate 150 replies in time.
   - **Calibration**: Tested judge agreement with 30 human-labelled examples (Cohen's k=0.68)
   - **Caveat**: LLM judge might be lenient on LLM-generated replies (potential bias)

### 13. **Two Baselines: Trivial + Simple (Not State-of-Art)**
   - **Decision**: Didn't implement BERT fine-tuned baseline
   - **Why**: Assignment asks for "trivial and simple" baselines. Those reveal the delta. State-of-art would be useful but overkill for proving concept.
   - **Trade-off**: Easier to beat simple baselines, but numbers are honest about real-world utility

### 14. **Stored Resolution Patterns Manually**
   - **Decision**: Hardcoded Apple solutions instead of scraping or using retrieved corpus
   - **Why**: Faster to implement, ensures correctness. Real system would do retrieval from docs.
   - **Scale**: Would need sentence embedding + vector DB for production

### 15. **README First, Report Last**
   - **Decision**: Build runnable code that demo's results in <15 min, write narrative report after
   - **Why**: "Proof is worth more than system" - actual working demo beats perfect paper
   - **Priority**: Reproducibility > polish
