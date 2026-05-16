# The Impact of AI Adoption on Job Growth and Automation Risk

This reproducible research project analyses a synthetic job-market dataset to understand how AI adoption relates to job growth, automation risk, and required skills.

## Research questions

1. How does AI adoption affect job growth?
2. How is AI adoption related to automation risk?
3. Which skills are associated with high-growth and low-automation-risk jobs?

## Project structure

```text
reproducible_ai_jobs_project/
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned dataset created by scripts
├── scripts/                  # Reproducible Python scripts
├── outputs/
│   ├── figures/              # Saved visualizations
│   └── tables/               # Saved summary tables
├── docs/                     # Notes, report drafts, presentation material
├── requirements.txt          # Python packages needed
└── README.md                 # Project description and instructions
```

## Reproducibility instructions

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate   # Mac/Linux
```

Install packages:

```bash
pip install -r requirements.txt
```

Run the project from the main project folder:

```bash
python scripts/01_clean_data.py
python scripts/02_visualizations.py
python scripts/03_correlation_and_skills.py
```

The cleaned dataset will be saved in `data/processed/`. Tables and charts will be saved in `outputs/`.

## Task distribution

**Langelihle Magwali**
- Data cleaning and preprocessing
- Exploratory data analysis
- Visualizations
- GitHub project structure and file organization

**Chiedza H. Chimedza**
- Correlation analysis
- Skills analysis
- Interpretation of results
- Discussion and conclusions

## Suggested visualizations

- Bar chart of job growth distribution
- Bar chart of automation risk distribution
- Grouped bar chart of AI adoption level vs automation risk
- Grouped bar chart of AI adoption level vs job growth projection
- Bar chart of average job growth score by industry
- Bar chart of skills found in high-growth, low-risk jobs
- Stacked percentage bar chart of job growth by job title

Pie charts can be used for a simple overview, but bar charts are usually clearer when comparing many job titles or categories.

## GitHub workflow

After cloning the GitHub repository and copying these files into it:

```bash
git status
git add .
git commit -m "Add reproducible AI job market analysis"
git push origin main
```

If your branch is called `master`, use:

```bash
git push origin master
```
