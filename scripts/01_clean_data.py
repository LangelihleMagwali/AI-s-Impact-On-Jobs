from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = ROOT / "data" / "raw" / "ai_job_market_insights.csv"
PROCESSED_DATA = ROOT / "data" / "processed" / "ai_job_market_clean.csv"


def main():
    df = pd.read_csv(RAW_DATA)
    df.columns = [col.strip().lower() for col in df.columns]
    df = df.drop_duplicates()
    df["salary_usd"] = df["salary_usd"].round(2)
    PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA, index=False)
    print(f"Saved cleaned data to {PROCESSED_DATA}")
    print(df.info())


if __name__ == "__main__":
    main()
