# Analysis Notes

## Dataset
The dataset contains 500 synthetic job listings with variables such as job title, industry, AI adoption level, automation risk, required skills, salary, remote-friendly status, and job growth projection.

## Main analysis logic

1. Clean the dataset by standardising column names and checking missing values.
2. Explore job growth, automation risk, industry, and skill distributions.
3. Compare AI adoption levels with job growth and automation risk.
4. Filter for jobs that are both high-growth and low-risk.
5. Count the most common skills in those filtered jobs.
6. Convert ordered categories into numeric scores for correlation analysis.

## Research Questions

- Which job growth category is most common?
- Which automation risk category appears most often?
- Do high AI adoption jobs show more growth, more decline, or a mix?
- Which skills appear most often in jobs that are growing and have low automation risk?
- Which industries have the highest average growth score?
