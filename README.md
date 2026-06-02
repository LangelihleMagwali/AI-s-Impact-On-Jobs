# The Impact of AI Adoption on Job Growth and Automation Risk

This reproducible research project analyses a synthetic job-market dataset to
understand how AI adoption relates to job growth, automation risk, and required
skills across 500 job listings.

## Research questions

1. How does AI adoption affect job growth?
2. How is AI adoption related to automation risk?
3. Which skills are associated with high-growth and low-automation-risk jobs?

## Project structure

```text
AI-s-Impact-On-Jobs/
├── data/
│   ├── raw/                        # Original dataset
│   └── processed/                  # Cleaned dataset (created by script 01)
├── scripts/
│   ├── 01_clean_data.py            # Data cleaning and preprocessing
│   ├── 02_visualizations.py        # Exploratory visualizations
│   ├── 03_correlation_and_skills.py  # Correlation matrix and skills analysis
│   └── 04_regression_and_clustering.py  # Linear regression and K-Means clustering
├── outputs/
│   ├── figures/                    # All saved charts and plots
│   └── tables/                     # All saved summary CSV tables
├── docs/
│   ├── analysis_notes.md           # Dataset and analysis logic notes
│   └── interpretation.md           # Written interpretation of all results
├── requirements.txt                # Python packages needed
└── README.md
```

## Reproducibility instructions

### 1. Clone the repository

```bash
git clone https://github.com/LangelihleMagwali/AI-s-Impact-On-Jobs.git
cd AI-s-Impact-On-Jobs
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run all scripts in order

```bash
python scripts/01_clean_data.py
python scripts/02_visualizations.py
python scripts/03_correlation_and_skills.py
python scripts/04_regression_and_clustering.py
```

All scripts must be run from the **root project folder**. The cleaned dataset
is saved to `data/processed/`. All figures and tables are saved to `outputs/`.

## Analysis overview

| Script | What it does | Author |
|---|---|---|
| `01_clean_data.py` | Standardises column names, removes duplicates | Langelihle |
| `02_visualizations.py` | Bar charts and distributions for EDA | Langelihle |
| `03_correlation_and_skills.py` | Ordinal encoding, correlation matrix, skills in high-growth/low-risk jobs | Chiedza |
| `04_regression_and_clustering.py` | Linear regression (AI adoption → job growth / automation risk), K-Means clustering (k=3) | Chiedza |

Full written interpretation of results is in `docs/interpretation.md`.

## Task distribution

**Langelihle Magwali**
- Data cleaning and preprocessing (`01_clean_data.py`)
- Exploratory data analysis and visualizations (`02_visualizations.py`)
- GitHub project structure and file organisation

**Chiedza H. Chimedza**
- Correlation analysis and skills analysis (`03_correlation_and_skills.py`)
- Linear regression and K-Means clustering (`04_regression_and_clustering.py`)
- Interpretation of results (`docs/interpretation.md`)

## GitHub workflow

We follow a branch-and-pull-request workflow:

1. Each team member works on their own branch (e.g. `chiedza-analysis`)
2. Changes are committed with descriptive messages as work progresses
3. A pull request is opened for the other member to review before merging to `main`

```bash
# Example: creating and pushing a feature branch
git checkout -b chiedza-analysis
git add scripts/04_regression_and_clustering.py
git commit -m "Add regression and clustering analysis script"
git push origin chiedza-analysis
```
