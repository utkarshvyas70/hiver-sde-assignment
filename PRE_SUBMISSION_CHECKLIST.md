# Pre-Submission Checklist for Hiver Assignment

Use this checklist to verify everything is ready before you submit.

---

## LOCAL SETUP ✓

- [ ] Python 3.8+ installed
- [ ] OpenAI API key generated (from https://platform.openai.com/account/api-keys)
- [ ] Project folder downloaded/organized

---

## CODE VERIFICATION ✓

### Dependencies
- [ ] `requirements.txt` exists with all packages listed
- [ ] Can run: `pip install -r requirements.txt` without errors
- [ ] No version conflicts (test in fresh virtual environment)

### Core Files Present
- [ ] `src/support_agent.py` - Main agent implementation
- [ ] `src/__init__.py` - Package init file
- [ ] `evaluate.py` - Evaluation harness
- [ ] `test_agent.py` - Quick demo script
- [ ] `config.json` - Configuration file

### Data Files
- [ ] `data/golden_eval_set.json` - 150 labelled examples
- [ ] File has correct structure (metadata + examples array)
- [ ] All 150 examples have required fields

### Configuration
- [ ] `.env` file created locally (not in git): `OPENAI_API_KEY=sk-xxx`
- [ ] `.gitignore` includes `.env` and `__pycache__/`
- [ ] `config.json` has all settings configured

---

## TESTING ✓

### Basic Functionality
- [ ] Set environment variable: `export OPENAI_API_KEY="your-key"`
- [ ] Run: `python test_agent.py`
  - [ ] Produces output for all 8 test messages
  - [ ] No errors or exceptions
  - [ ] Output format correct (intent, reply, escalate, reason)
- [ ] Run: `python evaluate.py`
  - [ ] Completes without errors
  - [ ] Takes <5 minutes to run
  - [ ] Prints results to console
  - [ ] Creates `results/evaluation_results.json`

### Code Quality
- [ ] No syntax errors: `python -m py_compile src/support_agent.py`
- [ ] No syntax errors: `python -m py_compile evaluate.py`
- [ ] Imports work: `python -c "from src.support_agent import SupportAgent"`

### Results Sanity Check
- [ ] Intent accuracy is 60-85% (78% expected)
- [ ] Escalation F1 is 0.6-0.8 (0.72 expected)
- [ ] Results file created successfully
- [ ] Can open and read JSON results

---

## DOCUMENTATION ✓

### README.md
- [ ] Exists and is readable
- [ ] Contains "Overview" section
- [ ] "Quick Start" section exists with:
  - [ ] Installation instructions
  - [ ] API key setup
  - [ ] How to run evaluation
  - [ ] Expected output/timeline
- [ ] "Project Structure" section
- [ ] "Results" section with headline numbers
- [ ] "Dataset" section
- [ ] "Baselines Compared" section
- [ ] Can understand whole project from README alone

### ASSIGNMENT_REPORT.docx
- [ ] File exists and can be opened in Word/Google Docs
- [ ] Contains all 10 sections:
  1. [ ] Problem Framing
  2. [ ] Approach & Solution
  3. [ ] Data & Evaluation Setup
  4. [ ] Results vs Baselines
  5. [ ] Top 5 Failure Modes
  6. [ ] Misleading Numbers Section (MANDATORY)
  7. [ ] If I Had One More Week
  8. [ ] What I Actually Did (Walkthrough)
  9. [ ] Code Quality & Reproducibility
  10. [ ] Final Thoughts
- [ ] No spelling/grammar errors
- [ ] Professional but readable tone
- [ ] Human-written (not ChatGPT sounding)
- [ ] Under 6 pages

### DECISION_LOG.md
- [ ] File exists and is markdown
- [ ] Contains 10-15 decisions with:
  - [ ] Decision name
  - [ ] What was decided
  - [ ] Why (reasoning)
  - [ ] Trade-offs considered
- [ ] Decisions are non-obvious (not "I used Python" level)
- [ ] Shows good judgment and trade-off thinking

### Other Docs
- [ ] `config.json` is valid JSON and readable
- [ ] `requirements.txt` properly formatted (one package per line)
- [ ] `.gitignore` includes `.env`, `__pycache__/`, `*.pyc`

---

## GIT SETUP ✓

### Local Git Repo
- [ ] `.git` folder exists in project root
- [ ] Run: `git status`
  - [ ] Shows modified files (not errors)
  - [ ] On `main` or `master` branch
- [ ] Run: `git log`
  - [ ] Shows at least one commit
- [ ] `.env` is NOT in `git status` (should be gitignored)
- [ ] All important files ARE in `git status`

### Commit History
- [ ] At least 1 commit: `git log --oneline`
- [ ] Commit message is clear (e.g., "Initial commit: Customer support AI agent")
- [ ] Can run: `git show HEAD` and see meaningful changes

---

## GITHUB SETUP ✓

### Repository Created
- [ ] GitHub account exists and logged in
- [ ] New repository created: `hiver-sde-assignment` (or similar)
- [ ] Repository is set to **PUBLIC** (not private)
- [ ] Go to `Settings > General` and verify "Public"
- [ ] Repository URL looks like: `https://github.com/YourUsername/hiver-sde-assignment`

### Code Pushed
- [ ] Added remote: `git remote -v` shows origin URL
- [ ] Pushed to main: `git push -u origin main` executed
- [ ] No errors during push
- [ ] Go to GitHub repo in browser and see:
  - [ ] README.md visible on homepage
  - [ ] `src/` folder with `support_agent.py`
  - [ ] `data/` folder with `golden_eval_set.json`
  - [ ] `evaluate.py` file
  - [ ] Other key files all present
- [ ] `.env` NOT visible (should not be pushed)
- [ ] Can see file contents by clicking on them

### Repo Cleanliness
- [ ] No `__pycache__/` folders visible
- [ ] No `.pyc` files visible
- [ ] No `results/` folder with old test runs
- [ ] No API keys or secrets visible anywhere
- [ ] `.gitignore` is working correctly

---

## HIVER SUBMISSION PREP ✓

### Information Gathered
- [ ] Full name ready
- [ ] Email address ready
- [ ] GitHub repository URL copied: 
  ```
  https://github.com/YourUsername/hiver-sde-assignment
  ```
- [ ] Bookmark to Hiver submission form saved:
  ```
  https://intelligent-bar-256.notion.site/39492cbf0da2800682cfc78a600a745f
  ```

### Report Attachment
- [ ] ASSIGNMENT_REPORT.docx ready to attach/upload
- [ ] File size is reasonable (<5MB)
- [ ] Can open the file to verify contents

### Submission Message Ready
Prepare something like this to paste:

```
GitHub Repository: https://github.com/YourUsername/hiver-sde-assignment

Assignment Details:
- Intent Classification Accuracy: 78%
- Escalation F1 Score: 0.72
- Golden Dataset: 150 hand-labelled examples
- Evaluation: Compared against trivial and keyword baselines

To Reproduce:
1. Clone the repo
2. export OPENAI_API_KEY="your-key"
3. pip install -r requirements.txt
4. python evaluate.py

Results completed in under 5 minutes. Full report and decision log included in repo.
```

---

## FINAL VERIFICATION ✓

### Does Everything Work?
- [ ] Locally tested code: ✓
- [ ] Code runs in <15 minutes: ✓
- [ ] GitHub repo accessible: ✓
- [ ] All files present and readable: ✓
- [ ] Documentation complete: ✓
- [ ] No API keys visible: ✓

### Will Hiver Be Able To:
- [ ] Access GitHub repo? (test in incognito browser or different account)
- [ ] Read README.md? Yes
- [ ] Understand how to run the code? Yes
- [ ] Run the code themselves? Yes (with their own API key)
- [ ] See results in <15 minutes? Yes
- [ ] Read the full report? Yes
- [ ] Understand your decision-making? Yes

### Are You Confident About:
- [ ] Explaining the code to someone? Yes
- [ ] Defending your decisions? Yes
- [ ] Answering questions about failure modes? Yes
- [ ] Discussing limitations honestly? Yes
- [ ] Explaining why certain tradeoffs were made? Yes

---

## RED FLAGS TO AVOID ❌

- [ ] ❌ Do NOT include your real API key in code or in git
- [ ] ❌ Do NOT make the repo private
- [ ] ❌ Do NOT leave `__pycache__/` or `.pyc` files in git
- [ ] ❌ Do NOT have dead code or commented-out sections
- [ ] ❌ Do NOT make results sound better than they are
- [ ] ❌ Do NOT skip the "What's misleading" section
- [ ] ❌ Do NOT pretend you know things you don't
- [ ] ❌ Do NOT push without testing locally first
- [ ] ❌ Do NOT submit if code has obvious bugs or errors

---

## SUBMISSION FLOW

### Day Before Submission
- [ ] Run through this entire checklist
- [ ] Fix any issues found
- [ ] Re-test everything
- [ ] Sleep well

### Day Of Submission
- [ ] Final check: code runs locally ✓
- [ ] Final check: repo is public ✓
- [ ] Final check: all files present ✓
- [ ] Open Hiver form
- [ ] Paste GitHub link
- [ ] Attach/link ASSIGNMENT_REPORT.docx
- [ ] Add submission message
- [ ] Hit submit
- [ ] ✓ DONE

### After Submission
- [ ] Check email (even spam folder) for confirmation
- [ ] Screenshot the confirmation
- [ ] Keep the folder handy (they might ask for tweaks)
- [ ] Be ready for technical interview
- [ ] Review DECISION_LOG.md one more time

---

## QUICK TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Code won't run locally | Check API key is set: `echo $OPENAI_API_KEY` |
| `ModuleNotFoundError` | Run: `pip install -r requirements.txt` |
| Code runs but no output | Check if network connection is stable |
| Results different from expected | Normal variation. Document what you got. |
| Can't push to GitHub | Generate Personal Access Token, use as password |
| Repo shows as private | Settings > Danger Zone > Change visibility to Public |
| Can't see `.env` in git (good!) | Means `.gitignore` is working correctly |
| README doesn't show on GitHub | Refresh page or check filename is exactly `README.md` |

---

## Timeline

- **30 mins**: Work through this checklist
- **5 mins**: Fix any issues
- **5 mins**: Final test
- **5 mins**: Submit
- **Total: ~45 minutes** to go from here to submission

---

## Questions to Ask Yourself Before Hitting Submit

1. **Can I explain this code to someone?** Yes / No → If No, simplify or document better
2. **Am I honest about limitations?** Yes / No → If No, add more detail to report
3. **Would I want to defend these decisions?** Yes / No → If No, reconsider them
4. **Have I tested this locally?** Yes / No → If No, do it now
5. **Is my repo public?** Yes / No → If No, change it
6. **Do I understand what I built?** Yes / No → If No, go reread the code

---

## YOU'RE READY WHEN...

- [x] All items above are checked
- [x] Code runs without errors
- [x] GitHub repo is public and has all files
- [x] Documentation is clear and complete
- [x] You've tested everything locally
- [x] You understand your own work
- [x] You can talk about your decisions

**If all above are true: HIT SUBMIT! 🚀**

Good luck!
