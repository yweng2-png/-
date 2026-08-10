### Missing Value Imputation Strategy

Before imputing missing values, an EDA pass was run to check skewness, histogram shape,
and IQR-based outliers for each field with missing data — rather than defaulting to mean
imputation across the board.

- **Purchase_Amount** (skew = 3.343, 485 outliers / 9.6%): severe right-skew driven by a
  small group of high-value customers → imputed with **median** to avoid inflating values
  toward outlier-driven averages.
- **Review_Rating** (skew = -0.604, 0 outliers): mild left-skew but mean and median are
  nearly identical (3.67 vs 3.70) → imputed with **median**.
- **Previous_Purchases** (skew = 0.005, 0 outliers): symmetric distribution → imputed with
  **mean**, consistent with standard practice for non-skewed data.

The three diagnostics (skewness, distribution shape, outlier detection) converged on the
same conclusions, confirming the imputation strategy was data-driven rather than assumed.