## Discussion of Visualisations and Findings

This section discusses the graphs created during the exploratory data analysis. The purpose of these visualisations is to understand how AI adoption is related to job growth, automation risk, industry differences, and required skills.

---

### 1. Job Growth Projection Distribution

![Job Growth Projection Distribution](outputs/figures/job_growth_distribution.png)

This graph shows the overall distribution of job growth projections in the dataset. The three categories are **Decline**, **Stable**, and **Growth**.

From the graph, the number of jobs in each category appears to be fairly balanced. There are slightly more jobs in the **Decline** and **Growth** categories, while the **Stable** category is slightly lower. This suggests that the dataset contains a good mix of jobs that are expected to grow, remain stable, or decline.

This graph is useful because it gives a general overview of the labour market situation in the dataset before looking at more detailed relationships.

---

### 2. Automation Risk Distribution

![Automation Risk Distribution](outputs/figures/automation_risk_distribution.png)

This graph shows how jobs are distributed across the three automation risk levels: **Low**, **Medium**, and **High**.

The graph shows that **Medium automation risk** has the highest number of jobs, followed closely by **High automation risk**. **Low automation risk** has the lowest number of jobs, although the difference is not extremely large.

This suggests that many jobs in the dataset face at least some level of automation risk. It also shows that automation risk is an important factor to consider when analysing the future of work, because a large number of jobs may be affected by AI and automation technologies.

---

### 3. AI Adoption Level vs Job Growth

![AI Adoption Level vs Job Growth](outputs/figures/ai_adoption_vs_job_growth.png)

This grouped bar chart compares **AI adoption level** with **job growth projection**. The AI adoption categories are **Low**, **Medium**, and **High**, while job growth is divided into **Decline**, **Growth**, and **Stable**.

For jobs with **low AI adoption**, the number of jobs in the **Growth** and **Stable** categories is slightly higher than the number of jobs in **Decline**. For jobs with **medium AI adoption**, both **Growth** and **Decline** are high, while **Stable** is slightly lower. For jobs with **high AI adoption**, **Decline** appears higher than **Growth** and **Stable**.

This suggests that higher AI adoption does not automatically mean higher job growth. In this dataset, jobs with high AI adoption may also be more exposed to decline. However, medium AI adoption appears to have both growth and decline, meaning the relationship between AI adoption and job growth is not simple.

This graph helps answer the research question: **How does AI adoption affect job growth?**

---

### 4. AI Adoption Level vs Automation Risk

![AI Adoption Level vs Automation Risk](outputs/figures/ai_adoption_vs_automation_risk.png)

This graph compares **AI adoption level** with **automation risk**. It shows how many jobs fall into low, medium, or high automation risk within each AI adoption level.

For jobs with **low AI adoption**, the three automation risk categories are relatively close, with low and medium risk slightly higher. For **medium AI adoption**, high automation risk is the largest group. For **high AI adoption**, medium automation risk appears to be the highest, while low automation risk is the lowest.

This suggests that jobs with medium and high levels of AI adoption may still experience notable automation risk. The graph shows that AI adoption and automation risk are related, but the relationship is not perfectly direct. Some jobs with high AI adoption may still be medium risk rather than high risk.

This graph helps answer the research question: **How is AI adoption related to automation risk?**

---

### 5. Average Job Growth Score by Industry

![Average Job Growth Score by Industry](outputs/figures/industry_growth_score.png)

This graph shows the average job growth score for each industry. The growth score was coded as:

- **0 = Decline**
- **0.5 = Stable**
- **1 = Growth**

A higher score means that an industry has more jobs projected to grow.

The graph shows that **Finance** has the highest average job growth score, followed by **Education**, **Transportation**, and **Telecommunications**. Industries such as **Energy** and **Retail** have lower average growth scores.

This suggests that some industries may be more positively affected by AI-related changes than others. For example, industries like finance and education may be benefiting from AI adoption through improved data analysis, automation of routine tasks, and demand for digital skills.

This graph helps identify which industries may have stronger future job opportunities.

---

### 6. Skills in High-Growth, Low-Risk Jobs

![Skills in High-Growth, Low-Risk Jobs](outputs/figures/high_growth_low_risk_skills.png)

This graph focuses only on jobs that are both **high-growth** and **low automation risk**. It shows which skills appear most often in these safer and growing jobs.

The most common skills in this group are **UX/UI Design** and **Machine Learning**, followed by **Python**, **Cybersecurity**, **Sales**, and **Data Analysis**.

This suggests that both technical and human-centred skills are important in jobs that are expected to grow while remaining less vulnerable to automation. Technical skills such as **Machine Learning**, **Python**, **Cybersecurity**, and **Data Analysis** are useful because they support digital transformation. At the same time, skills like **UX/UI Design**, **Sales**, and **Communication** remain valuable because they require creativity, problem-solving, and human interaction.

This graph helps answer the research question: **Which skills are associated with high-growth and low-automation-risk jobs?**

---

### 7. Job Growth Percentages by Job Title

![Job Growth Percentages by Job Title](outputs/figures/job_growth_percentages_by_title.png)

This stacked bar chart shows the percentage of jobs in each growth category for different job titles. Each bar adds up to 100%, showing the proportion of jobs projected to **Decline**, remain **Stable**, or experience **Growth**.

The graph shows that job titles such as **Operations Manager**, **Product Manager**, and **Software Engineer** have relatively strong growth percentages. On the other hand, some roles such as **Marketing Specialist** and **HR Manager** show higher proportions of decline or stability.

This graph is useful because it gives a more detailed view than the overall job growth distribution. Instead of only showing how many jobs are growing or declining overall, it shows which specific job titles may be more likely to grow or decline.

This visualisation is also better than a pie chart because it allows several job titles to be compared at once.

---

## Overall Interpretation

Overall, the graphs show that AI adoption affects jobs in different ways. The results do not suggest that AI adoption always leads to job growth or always leads to decline. Instead, the impact depends on the type of job, the industry, the level of automation risk, and the skills required.

The analysis shows that many jobs have medium or high automation risk, meaning that automation is an important issue in the labour market. However, there are also jobs that are growing and have low automation risk. These jobs often require skills such as UX/UI Design, Machine Learning, Python, Cybersecurity, Sales, and Data Analysis.

The industry analysis shows that Finance, Education, Transportation, and Telecommunications have stronger average job growth scores, while Retail and Energy show lower growth scores. This suggests that the effects of AI may differ across industries.

In conclusion, AI adoption is not only a threat to jobs. It can also create opportunities, especially for workers who develop relevant digital, analytical, creative, and communication skills.
