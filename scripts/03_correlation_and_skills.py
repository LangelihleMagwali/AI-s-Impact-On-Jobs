from pathlib import Path
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "ai_job_market_clean.csv"
TABLE_DIR = ROOT / "outputs" / "tables"
TABLE_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = pd.read_csv(DATA)

    ordered = df[["ai_adoption_level", "automation_risk", "job_growth_projection"]].copy()
    encoder = OrdinalEncoder(categories=[
        ["Low", "Medium", "High"],
        ["Low", "Medium", "High"],
        ["Decline", "Stable", "Growth"],
    ])
    encoded = pd.DataFrame(
        encoder.fit_transform(ordered),
        columns=["ai_adoption_score", "automation_risk_score", "job_growth_score"],
    )
    encoded["salary_usd"] = df["salary_usd"]
    corr = encoded.corr()
    corr.to_csv(TABLE_DIR / "correlation_matrix.csv")

    high_growth_low_risk = df[(df["job_growth_projection"] == "Growth") & (df["automation_risk"] == "Low")]
    skill_counts = high_growth_low_risk["required_skills"].value_counts()
    skill_counts.to_csv(TABLE_DIR / "skills_high_growth_low_risk.csv", header=["count"])

    print("Correlation matrix:")
    print(corr)
    print("Top skills in high-growth, low-risk jobs:")
    print(skill_counts.head(10))


if __name__ == "__main__":
    main()
