from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "ai_job_market_clean.csv"
FIG_DIR = ROOT / "outputs" / "figures"
TABLE_DIR = ROOT / "outputs" / "tables"
FIG_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)

AI_ORDER = ["Low", "Medium", "High"]
RISK_ORDER = ["Low", "Medium", "High"]
GROWTH_ORDER = ["Decline", "Stable", "Growth"]


def save_bar(series, title, xlabel, ylabel, filename, rotation=0):
    plt.figure(figsize=(8, 5))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation, ha="right" if rotation else "center")
    plt.tight_layout()
    plt.savefig(FIG_DIR / filename, dpi=150)
    plt.close()


def main():
    df = pd.read_csv(DATA)

    save_bar(
        df["job_growth_projection"].value_counts().reindex(GROWTH_ORDER),
        "Job Growth Projection Distribution",
        "Job growth projection",
        "Number of jobs",
        "job_growth_distribution.png",
    )

    save_bar(
        df["automation_risk"].value_counts().reindex(RISK_ORDER),
        "Automation Risk Distribution",
        "Automation risk",
        "Number of jobs",
        "automation_risk_distribution.png",
    )

    risk_table = pd.crosstab(df["ai_adoption_level"], df["automation_risk"]).reindex(AI_ORDER)
    risk_table.to_csv(TABLE_DIR / "ai_adoption_vs_automation_risk.csv")
    plt.figure(figsize=(8, 5))
    risk_table.plot(kind="bar", ax=plt.gca())
    plt.title("AI Adoption Level vs Automation Risk")
    plt.xlabel("AI adoption level")
    plt.ylabel("Number of jobs")
    plt.legend(title="Automation risk")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "ai_adoption_vs_automation_risk.png", dpi=150)
    plt.close()

    growth_table = pd.crosstab(df["ai_adoption_level"], df["job_growth_projection"]).reindex(AI_ORDER)
    growth_table.to_csv(TABLE_DIR / "ai_adoption_vs_job_growth.csv")
    plt.figure(figsize=(8, 5))
    growth_table.plot(kind="bar", ax=plt.gca())
    plt.title("AI Adoption Level vs Job Growth")
    plt.xlabel("AI adoption level")
    plt.ylabel("Number of jobs")
    plt.legend(title="Job growth")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "ai_adoption_vs_job_growth.png", dpi=150)
    plt.close()

    industry_growth = (
        df.assign(growth_numeric=df["job_growth_projection"].map({"Growth": 1, "Stable": 0.5, "Decline": 0}))
        .groupby("industry")["growth_numeric"]
        .mean()
        .sort_values(ascending=False)
    )
    industry_growth.to_csv(TABLE_DIR / "industry_growth_score.csv", header=["growth_score"])
    save_bar(
        industry_growth,
        "Average Job Growth Score by Industry",
        "Industry",
        "Growth score: 0=decline, 0.5=stable, 1=growth",
        "industry_growth_score.png",
        rotation=45,
    )

    high_growth_low_risk = df[(df["job_growth_projection"] == "Growth") & (df["automation_risk"] == "Low")]
    skill_counts = high_growth_low_risk["required_skills"].value_counts()
    skill_counts.to_csv(TABLE_DIR / "high_growth_low_risk_skill_counts.csv", header=["count"])
    save_bar(
        skill_counts,
        "Skills in High-Growth, Low-Risk Jobs",
        "Required skill",
        "Number of jobs",
        "high_growth_low_risk_skills.png",
        rotation=45,
    )

    job_growth_pct = pd.crosstab(
        df["job_title"], df["job_growth_projection"], normalize="index"
    ).reindex(columns=GROWTH_ORDER).fillna(0) * 100
    job_growth_pct.to_csv(TABLE_DIR / "job_title_growth_percentages.csv")
    plt.figure(figsize=(10, 6))
    job_growth_pct.plot(kind="bar", stacked=True, ax=plt.gca())
    plt.title("Job Growth Percentages by Job Title")
    plt.xlabel("Job title")
    plt.ylabel("Percentage of jobs")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Growth projection")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "job_growth_percentages_by_title.png", dpi=150)
    plt.close()

    print(f"Saved figures to {FIG_DIR}")
    print(f"Saved tables to {TABLE_DIR}")


if __name__ == "__main__":
    main()
