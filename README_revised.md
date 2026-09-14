# Recycling Demand Forecasting — MSBA Practicum Project (Sponsor: PROMESA)

**Author**: Yujia Weng (William Weng) | Santa Clara University, Leavey School of Business — MS Business Analytics
**Team**: Mackenzie Lozada, Mrudhvika Sirineni, Yujia Weng
**Project Duration**: January 2026 – June 2026 | Santa Clara, California

## Project Background

An MSBA practicum project in partnership with the recycling services company **PROMESA**, which collects recyclables from 56 businesses, 132 schools, and 61 cafés in Mexico City on a **fixed pickup schedule**. The project's original two-stage goal was to (1) forecast monthly recycling volume per partner and (2) use those forecasts to optimize collection routes, enabling a shift toward **dynamic, volume-based scheduling**.

**Stage 2 (route optimization) was scoped but not implemented**, because the sponsor was unable to provide historical routing data. The team's deliverable is therefore the **predictive foundation (Stage 1)** — a working forecasting and classification pipeline that PROMESA could plug route data into in the future.

## My Role and Responsibilities

I independently owned the **business partner dataset** end-to-end (56 businesses, ~684 model rows after feature construction), and contributed to the overall analytical framework used across all three partner segments (schools, cafés, businesses):

- **Data Cleaning & Integration**: Used Python (Pandas) to clean and aggregate monthly recycling records for 56 business partners; standardized inconsistent date formats, handled missing values, and filtered outliers using the 95th-percentile threshold for visualization
- **Feature Engineering**: Built a sliding 6-month-window dataset (6 consecutive months as predictors, 7th month as target) to convert raw monthly time series into a supervised learning format
- **Predictive Modeling**: Trained a linear regression model to forecast next-month recycling volume per business — R² = 0.853 on held-out data (i.e., prior 6 months of volume explain ~85% of the variance in the following month's volume)
- **Classification Modeling & Model Selection**: Discretized predicted volumes into Low/Medium/High tiers using `pd.qcut()`; benchmarked Softmax Regression, Random Forest, and XGBoost — Softmax Regression performed best (accuracy/F1 ≈ 0.737)
- **Cross-Segment Framework Design**: Collaborated with teammates to apply the same sliding-window regression + tiered classification approach across the café dataset (R² = 0.88) and school dataset (R² = 0.334, constrained by only ~9 months of usable data per school — the team deliberately prioritized the classification approach over precise volume forecasting for this segment given the data limitation)
- **Stakeholder Communication**: Contributed to the final presentation delivered to PROMESA executives and academic advisors, including explicitly communicating the Stage 2 data gap and what would be needed to close it

## Key Results

| Segment | Model | Result | Note |
|---|---|---|---|
| Business (56 partners) | Linear Regression | R² = 0.853 | My primary dataset |
| Business (56 partners) | Softmax Classification (Low/Med/High) | Accuracy/F1 ≈ 0.737 | My primary dataset |
| Café (61 partners) | Linear Regression | R² = 0.88 | Team |
| School (132 partners) | Linear Regression | R² = 0.334 | Team; limited by ~9 months of data per school |
| School (132 partners) | Softmax Classification | Accuracy/F1 ≈ 0.741 | Team; classification preferred over point forecasting given limited history |

**What these numbers mean in practice**: for businesses and cafés, the model can reliably flag next month's expected volume tier with enough accuracy to inform planning conversations. For schools, data history was too short (9 months) to trust precise volume forecasts, so the team recommended relying on the tier classification instead.

## Honest Scope & Limitations

- **No route optimization was built.** The "dynamic scheduling" benefit is a **future-state recommendation**, not a delivered capability — it depends on PROMESA providing historical routing/GPS data, which was not available during this project.
- **No cost-savings figure was calculated.** Any dollar or efficiency estimate would require the routing layer that wasn't built; we did not fabricate one.
- **School-segment forecasts are directional, not precise**, due to short data history (9 months average vs. 14–18 months for cafés/businesses).
- External factors (holidays, local events, policy changes) were not incorporated into any of the models.

## What This Project Demonstrates

- Ability to independently own a full modeling pipeline (cleaning → feature engineering → model selection → evaluation) for a live external client
- Judgment to choose classification over regression when data volume didn't support precise forecasting (schools), rather than forcing an unreliable model
- Comfort communicating a project's real scope and limitations to stakeholders, rather than overstating delivered value

## File Descriptions

- [`Yujia Business Data Analysis-Copy1(1).ipynb`](./Yujia%20Business%20Data%20Analysis-Copy1(1).ipynb) — Complete data cleaning, modeling, and visualization code for the business dataset (Jupyter Notebook, viewable directly in browser)
- [`Final_Presentation.pdf`](./Final_Presentation.pdf) — Final project presentation deck delivered to PROMESA (PDF, previewable online)

## Tech Stack

Python (Pandas, NumPy, Scikit-learn, Matplotlib) · SQL · Linear Regression · Softmax Regression · XGBoost · Random Forest · Feature Engineering (sliding-window) · EDA

## Contact

📧 yweng2@scu.edu | 🔗 [LinkedIn](https://www.linkedin.com/in/william-weng-083ba9402)
