"""
Script 04: Linear Regression and K-Means Clustering
Author: Chiedza H. Chimedza
Description:
    Extends the correlation analysis with:
    1. Linear regression - quantifying the impact of AI adoption on job
       growth score and automation risk score.
    2. K-Means clustering - grouping jobs based on AI adoption, job growth,
       and automation risk to identify distinct labour-market segments.
    3. Interpretation summary saved to docs/interpretation.md
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OrdinalEncoder

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "ai_job_market_clean.csv"
TABLE_DIR = ROOT / "outputs" / "tables"
FIGURE_DIR = ROOT / "outputs" / "figures"
DOCS_DIR = ROOT / "docs"
TABLE_DIR.mkdir(parents=True, exist_ok=True)
FIGURE_DIR.mkdir(parents=True, exist_ok=True)
DOCS_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Helper: encode ordinal columns
# ---------------------------------------------------------------------------
def encode_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of df with ordinal columns replaced by numeric scores."""
    df = df.copy()
    encoder = OrdinalEncoder(
        categories=[
            ["Low", "Medium", "High"],
            ["Low", "Medium", "High"],
            ["Decline", "Stable", "Growth"],
        ]
    )
    encoded_vals = encoder.fit_transform(
        df[["ai_adoption_level", "automation_risk", "job_growth_projection"]]
    )
    df["ai_adoption_score"] = encoded_vals[:, 0]
    df["automation_risk_score"] = encoded_vals[:, 1]
    df["job_growth_score"] = encoded_vals[:, 2]
    return df


# ---------------------------------------------------------------------------
# 1. Linear Regression
# ---------------------------------------------------------------------------
def run_regression(df: pd.DataFrame) -> dict:
    """
    Fit two OLS regression models:
      - Model A: ai_adoption_score → job_growth_score
      - Model B: ai_adoption_score → automation_risk_score
    Returns a dict of results and saves coefficient tables.
    """
    results = {}
    models = {
        "job_growth": ("job_growth_score", "Job Growth Score"),
        "automation_risk": ("automation_risk_score", "Automation Risk Score"),
    }

    X = df[["ai_adoption_score"]]

    for key, (target_col, target_label) in models.items():
        y = df[target_col]
        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)

        r2 = r2_score(y, y_pred)
        mse = mean_squared_error(y, y_pred)
        coef = model.coef_[0]
        intercept = model.intercept_

        results[key] = {
            "target": target_label,
            "coefficient": round(coef, 6),
            "intercept": round(intercept, 6),
            "r2": round(r2, 6),
            "mse": round(mse, 6),
        }

        # Save coefficient table
        coef_df = pd.DataFrame(
            {
                "predictor": ["ai_adoption_score"],
                "coefficient": [round(coef, 6)],
                "intercept": [round(intercept, 6)],
                "r2": [round(r2, 6)],
                "mse": [round(mse, 6)],
            }
        )
        coef_df.to_csv(TABLE_DIR / f"regression_{key}.csv", index=False)

        # Scatter + regression line
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.scatter(
            df["ai_adoption_score"],
            y,
            alpha=0.3,
            color="#4C72B0",
            label="Observed",
        )
        x_line = pd.DataFrame({"ai_adoption_score": [0, 1, 2]})
        ax.plot(
            x_line["ai_adoption_score"],
            model.predict(x_line),
            color="#C44E52",
            linewidth=2,
            label=f"Regression line (R²={r2:.3f})",
        )
        ax.set_xticks([0, 1, 2])
        ax.set_xticklabels(["Low", "Medium", "High"])
        ax.set_xlabel("AI Adoption Level")
        ax.set_ylabel(target_label)
        ax.set_title(f"Linear Regression: AI Adoption → {target_label}")
        ax.legend()
        fig.tight_layout()
        fig.savefig(FIGURE_DIR / f"regression_{key}.png", dpi=150)
        plt.close(fig)
        print(f"  Regression ({key}): coef={coef:.4f}, R²={r2:.4f}")

    return results


# ---------------------------------------------------------------------------
# 2. K-Means Clustering
# ---------------------------------------------------------------------------
def run_clustering(df: pd.DataFrame, n_clusters: int = 3) -> pd.DataFrame:
    """
    Cluster jobs using K-Means on ai_adoption_score, job_growth_score,
    and automation_risk_score.
    Returns df with an added 'cluster' column and saves outputs.
    """
    features = ["ai_adoption_score", "job_growth_score", "automation_risk_score"]
    X = df[features]

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df = df.copy()
    df["cluster"] = kmeans.fit_predict(X)

    # Cluster profile summary
    profile = (
        df.groupby("cluster")[features + ["salary_usd"]]
        .mean()
        .round(3)
        .rename(
            columns={
                "ai_adoption_score": "avg_ai_adoption",
                "job_growth_score": "avg_job_growth",
                "automation_risk_score": "avg_automation_risk",
                "salary_usd": "avg_salary_usd",
            }
        )
    )
    profile["cluster_size"] = df["cluster"].value_counts().sort_index()
    profile.to_csv(TABLE_DIR / "cluster_profiles.csv")
    print("\n  Cluster profiles:")
    print(profile.to_string())

    # Elbow plot (inertia for k=1..6) to justify k=3
    inertias = []
    for k in range(1, 7):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X)
        inertias.append(km.inertia_)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(range(1, 7), inertias, marker="o", color="#4C72B0")
    ax.axvline(x=n_clusters, color="#C44E52", linestyle="--", label=f"Chosen k={n_clusters}")
    ax.set_xlabel("Number of Clusters (k)")
    ax.set_ylabel("Inertia (within-cluster sum of squares)")
    ax.set_title("Elbow Method — Choosing Optimal k")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "clustering_elbow.png", dpi=150)
    plt.close(fig)

    # Scatter: AI adoption vs job growth, coloured by cluster
    colours = ["#4C72B0", "#DD8452", "#55A868"]
    fig, ax = plt.subplots(figsize=(7, 5))
    for c in sorted(df["cluster"].unique()):
        subset = df[df["cluster"] == c]
        ax.scatter(
            subset["ai_adoption_score"],
            subset["job_growth_score"],
            alpha=0.5,
            color=colours[c],
            label=f"Cluster {c}",
        )
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["Low", "Medium", "High"])
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["Decline", "Stable", "Growth"])
    ax.set_xlabel("AI Adoption Level")
    ax.set_ylabel("Job Growth Projection")
    ax.set_title("K-Means Clusters: AI Adoption vs Job Growth")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "clustering_scatter.png", dpi=150)
    plt.close(fig)

    # Bar chart: cluster size
    fig, ax = plt.subplots(figsize=(5, 4))
    sizes = df["cluster"].value_counts().sort_index()
    ax.bar(
        [f"Cluster {i}" for i in sizes.index],
        sizes.values,
        color=colours[: len(sizes)],
    )
    ax.set_ylabel("Number of Jobs")
    ax.set_title("Jobs per Cluster")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "clustering_sizes.png", dpi=150)
    plt.close(fig)

    return df, profile


# ---------------------------------------------------------------------------
# 3. Write interpretation summary
# ---------------------------------------------------------------------------
def write_interpretation(regression_results: dict, cluster_profile: pd.DataFrame) -> None:
    """Save a plain-language interpretation of all findings to docs/."""
    corr_path = TABLE_DIR / "correlation_matrix.csv"
    corr = pd.read_csv(corr_path, index_col=0) if corr_path.exists() else None

    lines = [
        "# Interpretation of Results",
        "**Author: Chiedza H. Chimedza**",
        "",
        "## 1. Correlation Analysis",
        "",
    ]

    if corr is not None:
        ai_jg = corr.loc["ai_adoption_score", "job_growth_score"]
        ai_ar = corr.loc["ai_adoption_score", "automation_risk_score"]
        lines += [
            f"- Correlation between AI adoption and job growth score: **{ai_jg:.4f}**",
            f"- Correlation between AI adoption and automation risk score: **{ai_ar:.4f}**",
            "",
            "Both correlations are weak, suggesting that AI adoption level alone does not",
            "strongly determine whether a job is growing or at risk of automation. This",
            "indicates that sector, required skills, and company size may play a more",
            "important role.",
            "",
        ]

    lines += [
        "## 2. Linear Regression",
        "",
    ]
    for key, r in regression_results.items():
        lines += [
            f"### Model: AI Adoption → {r['target']}",
            f"- Coefficient: {r['coefficient']}",
            f"- Intercept: {r['intercept']}",
            f"- R²: {r['r2']}",
            f"- MSE: {r['mse']}",
            "",
            f"The R² of {r['r2']:.4f} confirms that AI adoption level explains very little",
            f"of the variance in {r['target'].lower()}. While the coefficient direction",
            "gives a sense of the relationship, the effect is not practically significant",
            "on its own. This supports the need for multi-variable analysis.",
            "",
        ]

    lines += [
        "## 3. K-Means Clustering",
        "",
        "Three clusters were identified based on AI adoption, job growth, and automation risk:",
        "",
    ]
    for idx, row in cluster_profile.iterrows():
        lines += [
            f"### Cluster {idx}  (n={int(row['cluster_size'])})",
            f"- Avg AI adoption score: {row['avg_ai_adoption']} (0=Low, 1=Med, 2=High)",
            f"- Avg job growth score: {row['avg_job_growth']} (0=Decline, 1=Stable, 2=Growth)",
            f"- Avg automation risk score: {row['avg_automation_risk']} (0=Low, 1=Med, 2=High)",
            f"- Avg salary: ${row['avg_salary_usd']:,.0f}",
            "",
        ]

    lines += [
        "## 4. Overall Conclusions",
        "",
        "1. AI adoption does not uniformly drive job growth or reduce automation risk —",
        "   the relationships are weak across the whole dataset.",
        "2. Clustering reveals distinct labour-market segments: some job groups combine",
        "   high AI adoption with growth (likely knowledge-work roles), while others",
        "   show high adoption alongside high automation risk (routine task roles).",
        "3. The skills most associated with high-growth, low-risk jobs include",
        "   UX/UI Design, Machine Learning, Python, and Cybersecurity — skills that",
        "   complement AI rather than compete with it.",
        "4. These findings align with labour economics research suggesting AI acts as a",
        "   complement to specialised human skills, not a simple replacement.",
        "",
        "## 5. Limitations",
        "",
        "- The dataset is synthetic (500 observations), so findings cannot be generalised",
        "  to real labour markets without validation on real data.",
        "- Single-variable regression ignores confounders such as industry and company size.",
        "- K-Means assumes spherical clusters and requires k to be specified in advance.",
    ]

    output = "\n".join(lines)
    out_path = DOCS_DIR / "interpretation.md"
    out_path.write_text(output, encoding="utf-8")
    print(f"\n  Interpretation saved to {out_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("Loading cleaned data ...")
    df = pd.read_csv(DATA)
    df = encode_dataframe(df)

    print("\n--- Linear Regression ---")
    reg_results = run_regression(df)

    print("\n--- K-Means Clustering (k=3) ---")
    df_clustered, cluster_profile = run_clustering(df, n_clusters=3)

    print("\n--- Writing interpretation ---")
    write_interpretation(reg_results, cluster_profile)

    print("\nAll outputs saved.")


if __name__ == "__main__":
    main()
