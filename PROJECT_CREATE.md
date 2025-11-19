🧱 AI/Kaggle Project Creation Guide

This guide explains the full workflow for creating a clean, professional, reproducible project for Kaggle competitions or standalone ML projects.
Use it whenever you want to start a new repository.

⸻

1️⃣ Create the Project Repository

mkdir kaggle-competitions
cd kaggle-competitions
git init

Recommended folder structure:

kaggle-competitions/
│
├── notebooks/          # Jupyter notebooks for exploration
├── src/                # Reusable helper code
│   └── kaggle_utils.py
│
├── data/               # All actual data files (ignored in Git)
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── models/             # Saved models (ignored in Git)
│
├── requirements.txt
├── .gitignore
└── README.md


⸻

2️⃣ Add .gitignore

# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
.env

# Jupyter
.ipynb_checkpoints/

# Data & models
data/
models/

This keeps your repo clean and prevents huge dataset files from being committed.

⸻

3️⃣ Create a Virtual Environment

python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

Install initial dependencies:

pip install --upgrade pip
pip install kaggle jupyter ipykernel numpy pandas scikit-learn matplotlib


⸻

4️⃣ Create a Dedicated IPython Kernel

python -m ipykernel install --user --name kaggle-competitions --display-name "Kaggle (ipython)"

This ensures your notebooks run in the correct environment.

⸻

5️⃣ Configure Kaggle API

Place kaggle.json in the appropriate directory:
	•	macOS/Linux: ~/.kaggle/kaggle.json
	•	Windows: C:\Users\<YOU>\.kaggle\kaggle.json

Set permissions (Linux/macOS):

chmod 600 ~/.kaggle/kaggle.json

Test:

kaggle competitions list | head


⸻

6️⃣ Create Helper Functions (src/kaggle_utils.py)

Use project-root detection so downloads always go to data/raw/:

from __future__ import annotations
from pathlib import Path
import subprocess, zipfile

# Detect project root based on this file location
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"

# ...download functions here...

This guarantees the dataset never ends up inside notebooks/.

⸻

7️⃣ Create Your First Notebook

Place notebooks in:

notebooks/

Example:

notebooks/titanic_baseline.ipynb

Open VS Code:

code .

Select kernel:
Kernels → Kaggle (ipython)

Then import your helpers:

from src.kaggle_utils import download_competition


⸻

8️⃣ Save Dependencies

pip freeze > requirements.txt

(Optional) clean it later to top-level packages only.

⸻

9️⃣ First Commit

git add .
git commit -m "Initial Kaggle project setup"

(Optional) push to GitHub:

git remote add origin https://github.com/<your-user>/kaggle-competitions.git
git branch -M main
git push -u origin main


⸻

🔁 Daily Workflow Summary

Every time you return to the repo:

cd kaggle-competitions
source .venv/bin/activate
code .
# In notebook: select kernel "Kaggle (ipython)"

You’re ready to work with Kaggle datasets, create baselines, and track your experiments.

⸻

🎉 Done

You now have a clean, reproducible, professional project setup — perfect for Kaggle and for building your portfolio.

If you want, I can also generate a competition notebook template you can copy for any new Kaggle challenge.