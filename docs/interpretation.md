# Interpretation of Results
**Author: Chiedza H. Chimedza**

## 1. Correlation Analysis

- Correlation between AI adoption and job growth score: **-0.0548**
- Correlation between AI adoption and automation risk score: **0.0421**

Both correlations are weak, suggesting that AI adoption level alone does not
strongly determine whether a job is growing or at risk of automation. This
indicates that sector, required skills, and company size may play a more
important role.

## 2. Linear Regression

### Model: AI Adoption → Job Growth Score
- Coefficient: -0.056331
- Intercept: 1.053289
- R²: 0.003
- MSE: 0.673972

The R² of 0.0030 confirms that AI adoption level explains very little
of the variance in job growth score. While the coefficient direction
gives a sense of the relationship, the effect is not practically significant
on its own. This supports the need for multi-variable analysis.

### Model: AI Adoption → Automation Risk Score
- Coefficient: 0.042542
- Intercept: 0.981755
- R²: 0.00177
- MSE: 0.652359

The R² of 0.0018 confirms that AI adoption level explains very little
of the variance in automation risk score. While the coefficient direction
gives a sense of the relationship, the effect is not practically significant
on its own. This supports the need for multi-variable analysis.

## 3. K-Means Clustering

Three clusters were identified based on AI adoption, job growth, and automation risk:

### Cluster 0  (n=149)
- Avg AI adoption score: 0.242 (0=Low, 1=Med, 2=High)
- Avg job growth score: 0.523 (0=Decline, 1=Stable, 2=Growth)
- Avg automation risk score: 0.671 (0=Low, 1=Med, 2=High)
- Avg salary: $93,709

### Cluster 1  (n=188)
- Avg AI adoption score: 0.92 (0=Low, 1=Med, 2=High)
- Avg job growth score: 1.899 (0=Decline, 1=Stable, 2=Growth)
- Avg automation risk score: 1.069 (0=Low, 1=Med, 2=High)
- Avg salary: $90,623

### Cluster 2  (n=163)
- Avg AI adoption score: 1.62 (0=Low, 1=Med, 2=High)
- Avg job growth score: 0.399 (0=Decline, 1=Stable, 2=Growth)
- Avg automation risk score: 1.288 (0=Low, 1=Med, 2=High)
- Avg salary: $89,641

## 4. Overall Conclusions

1. AI adoption does not uniformly drive job growth or reduce automation risk —
   the relationships are weak across the whole dataset.
2. Clustering reveals distinct labour-market segments: some job groups combine
   high AI adoption with growth (likely knowledge-work roles), while others
   show high adoption alongside high automation risk (routine task roles).
3. The skills most associated with high-growth, low-risk jobs include
   UX/UI Design, Machine Learning, Python, and Cybersecurity — skills that
   complement AI rather than compete with it.
4. These findings align with labour economics research suggesting AI acts as a
   complement to specialised human skills, not a simple replacement.

## 5. Limitations

- The dataset is synthetic (500 observations), so findings cannot be generalised
  to real labour markets without validation on real data.
- Single-variable regression ignores confounders such as industry and company size.
- K-Means assumes spherical clusters and requires k to be specified in advance.