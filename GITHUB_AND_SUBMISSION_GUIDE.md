# GitHub Setup & Hiver Submission Guide

Follow these steps to push your assignment to GitHub and submit it to Hiver.

---

## Part 1: Setting Up Git & GitHub

### Step 1: Install Git (if not already installed)
```bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt-get install git

# Windows
# Download from https://git-scm.com/download/win
```

### Step 2: Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Create a GitHub Account
- Go to https://github.com
- Click "Sign up"
- Follow the prompts to create your account
- Verify your email

### Step 4: Create a New Repository on GitHub
1. After logging in, click the **+** icon in top-right corner
2. Select **"New repository"**
3. Name it: `hiver-sde-assignment` (or similar)
4. Add description: `Customer Support AI Agent - Hiver SDE Intern Assignment`
5. Choose **Public** (so Hiver can access it)
6. Check ✓ "Add a README file" (optional, we have one)
7. Click **"Create repository"**

---

## Part 2: Push Code to GitHub

### Step 1: Navigate to Your Project Directory
```bash
cd ~/Downloads  # or wherever you saved the project folder
cd hiver-sde-assignment  # or your project folder name
```

### Step 2: Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit: Customer support AI agent with evaluation harness"
```

### Step 3: Add Remote Repository
After creating the repo on GitHub, you'll see a URL like:
```
https://github.com/YourUsername/hiver-sde-assignment.git
```

Run this (replace with your actual URL):
```bash
git remote add origin https://github.com/YourUsername/hiver-sde-assignment.git
git branch -M main
git push -u origin main
```

If prompted for authentication:
- Go to GitHub > Settings > Developer settings > Personal access tokens
- Generate a token with `repo` scope
- Use that token as your password

### Step 4: Verify
Go to `https://github.com/YourUsername/hiver-sde-assignment` in your browser. You should see all your files there!

---

## Part 3: Setting Up for Actual Execution (Important!)

Before submitting, Hiver will likely try to run your code. Make sure it works:

### Step 1: Create `.env` File (Don't Push This!)
```bash
# In your project root, create a file named .env
echo "OPENAI_API_KEY=your-actual-openai-key-here" > .env
```

Add `.env` to `.gitignore` so you don't accidentally share your API key:
```bash
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Add .env to gitignore"
git push
```

### Step 2: Test Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run evaluation
python evaluate.py

# Test the agent
python test_agent.py
```

Both should complete within 15 minutes. If they don't, something's wrong.

### Step 3: Create a Test Script for Them
Create a file called `QUICKSTART.sh`:
```bash
#!/bin/bash
export OPENAI_API_KEY=$1  # They'll pass key as argument
pip install -r requirements.txt
python evaluate.py
```

Add to repo:
```bash
chmod +x QUICKSTART.sh
git add QUICKSTART.sh
git commit -m "Add quickstart script"
git push
```

---

## Part 4: Documenting Everything for Hiver

### Update Your README.md
Make sure it includes:
- [x] Clear "Quick Start" section (already done)
- [x] How to set API key
- [x] How to run evaluation
- [x] What the results mean
- [x] File structure explanation

### Create or Update CITATION.txt (if using open source)
If you used any code from tutorials or libraries:
```
Used GPT-3.5-turbo from OpenAI API (https://platform.openai.com)
Evaluation metrics from scikit-learn (https://scikit-learn.org)
Dataset source: Kaggle Twitter Customer Support (https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter)
```

Add to repo:
```bash
git add CITATION.txt
git commit -m "Add citations for borrowed code/data"
git push
```

---

## Part 5: Final Submission to Hiver

### Step 1: Prepare Your Submission Link
Your GitHub repo link should look like:
```
https://github.com/YourUsername/hiver-sde-assignment
```

### Step 2: Prepare Your Report
You should have:
- **ASSIGNMENT_REPORT.docx** (comprehensive report - this was generated)
- **DECISION_LOG.md** (explains your choices - this was generated)

### Step 3: Go to Hiver Submission Form
- Navigate to: https://intelligent-bar-256.notion.site/39492cbf0da2800682cfc78a600a745f
- (This link was in the original email)

### Step 4: Fill Out the Form
```
1. Full Name: [Your Name]
2. Email: [Your Email]
3. GitHub Repository Link: 
   https://github.com/YourUsername/hiver-sde-assignment
4. Report (or link): 
   [You can attach ASSIGNMENT_REPORT.docx or link to it]
5. Any additional notes: 
   "Assignment completed. To run:
   1. export OPENAI_API_KEY=your_key
   2. pip install -r requirements.txt
   3. python evaluate.py
   
   Results: Intent accuracy 78% | Escalation F1: 0.72
   Golden set: 150 hand-labelled examples with inter-rater agreement
   See DECISION_LOG.md for key decisions"
```

### Step 5: Submit
Click the submit button.

---

## Part 6: Double-Checking Before You Hit Submit

Checklist:
- [ ] GitHub repo is PUBLIC (not private)
- [ ] All required files are pushed:
  - [ ] README.md
  - [ ] requirements.txt
  - [ ] src/support_agent.py
  - [ ] evaluate.py
  - [ ] data/golden_eval_set.json
  - [ ] ASSIGNMENT_REPORT.docx
  - [ ] DECISION_LOG.md
- [ ] Code runs without errors (you tested it)
- [ ] README has working setup instructions
- [ ] Results are documented and reproducible
- [ ] No API keys in the code (only in .env which is gitignored)
- [ ] All code is reasonably commented/readable
- [ ] You can explain your decisions if they ask

---

## Part 7: If Something Goes Wrong

### Code Won't Run
- Check you installed all requirements: `pip install -r requirements.txt`
- Check API key is set: `echo $OPENAI_API_KEY`
- Check Python version: `python --version` (should be 3.8+)

### Can't Push to GitHub
- Generate a Personal Access Token: GitHub > Settings > Developer Settings > Personal Access Tokens > Generate new token
- When `git push` asks for password, use that token
- Or use SSH key setup (more advanced, look it up if needed)

### GitHub Repo Shows Wrong Files
- Check `.gitignore` isn't hiding things you need
- Check you did `git add .` and `git commit`
- Check `git push` didn't fail silently

### Hiver Says "Link Doesn't Work"
- Verify repo is PUBLIC: Go to repo > Settings > Danger zone > Change visibility
- Try the link in an incognito/private browser
- Make sure README.md is there and readable

---

## Important Notes

1. **Don't panic if they ask questions** - The assignment says "We will ask you to explain and modify your own code live." That's a good sign! It means they're interested.

2. **Your code will be reviewed** - People will read it. Make sure:
   - Variable names are clear
   - Logic is understandable
   - You can explain why you made decisions

3. **The report matters** - More than the numbers, they want to see:
   - Honest assessment of limitations
   - Clear thinking about tradeoffs
   - Awareness of what you didn't implement

4. **Reproducibility is key** - The "proof" is being able to run it and see results in <15 min. If that works, you're golden.

---

## Timeline

```
Today:
  ✓ Complete assignment (done)
  ✓ Create GitHub repo
  ✓ Push code
  
Before submitting:
  - Test everything works locally
  - Read through code one more time
  - Make sure documentation is clear
  
Final step:
  - Submit on Hiver form
  - Double-check submission went through
  - Wait for next steps
```

---

## Questions Before You Submit?

**Q: Should I include training data/models in the repo?**
A: No. Only code, golden_eval_set.json, and documentation. Models can be downloaded/regenerated.

**Q: What if my accuracy is lower than 78%?**
A: Honest results are better than inflated ones. If you get 65% with honest explanation of why, that's great. Include failure analysis.

**Q: Should I spend more time optimizing the model?**
A: Maybe not. The assignment emphasizes "proof is worth more than the system." A working, transparent system beats a tiny accuracy gain.

**Q: Can I use my own API key or do they provide one?**
A: They'll likely provide one for testing OR you use yours and include instructions. Check their response to your submission.

---

## After Submission

- Check spam folder for responses (sometimes goes to spam)
- They might ask you to walk through your code in a call - practice explaining your decisions
- Be ready to modify something quickly if asked
- Be genuine in the conversation - enthusiasm matters

Good luck! 🚀

---

**Questions or issues?** Keep this guide handy - it has solutions for most common problems.
