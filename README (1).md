# Recycling Demand Forecasting — MSBA Practicum Project (Sponsor: PROMESA)

**Author**: Yujia Weng (William Weng) | Santa Clara University, Leavey School of Business — MS Business Analytics
**Project Duration**: January 2026 – June 2026 | Santa Clara, California

## Project Background

An MSBA practicum project in partnership with the recycling services company **PROMESA**. Using nearly 3 years of monthly recycling transaction data from 56 businesses, 132 schools, and 61 cafés, the project built predictive models to help the client transition from a **fixed pickup schedule** to a **dynamic, volume-based scheduling model**.

## My Role and Responsibilities

- **Data Cleaning & Integration**: Used Python (Pandas) to process monthly recycling data from 249 partner organizations, handling missing values and treating outliers using the 95th percentile threshold
- **Predictive Modeling**: Built a 6-month rolling-window linear regression model to forecast next-month recycling volume
- **Classification Modeling & Model Selection**: Used `pd.qcut()` to discretize recycling volume into High/Medium/Low tiers, then benchmarked Softmax Regression, XGBoost, and Random Forest
- **Data Visualization**: Used Matplotlib to create time-series trend charts, actual-vs-predicted scatter plots, and model comparison charts
- **Business Outcome Design**: Led the design of a three-tier classification early-warning system, shifting pickup planning from fixed scheduling to dynamic scheduling; proposed differentiated service strategies for different partner types (businesses/schools/cafés)
- **Stakeholder Communication**: Delivered the final presentation to sponsor company executives and academic advisors

## Key Results

| Metric | Result |
|---|---|
| Business dataset regression model | R² = 0.853 |
| Café dataset regression model | R² = 0.88 |
| School dataset regression model | R² = 0.334 (limited by insufficient historical data; classification approach preferred over precise value forecasting) |
| Softmax classification model | Accuracy / F1 ≈ 73.7% |

## File Descriptions

- [`Yujia Business Data Analysis-Copy1(1).ipynb`](./Yujia%20Business%20Data%20Analysis-Copy1(1).ipynb) — Complete data cleaning, modeling, and visualization code (Jupyter Notebook, viewable directly in browser)
- [`Final_Presentation.pdf`](./Final_Presentation.pdf) — Final project presentation deck (PDF, previewable online)

## Tech Stack

Python (Pandas, NumPy, Scikit-learn, Matplotlib) · SQL · Softmax Regression · XGBoost · Random Forest · Feature Engineering · EDA

## Contact

📧 yweng2@scu.edu | 🔗 [LinkedIn](https://www.linkedin.com/in/william-weng-083ba9402)
