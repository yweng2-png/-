## Business Recommendations & Implementation Roadmap

The analysis surfaces three independent, data-validated levers — each mapped to a
specific owner, action, and expected outcome.

### 1. Discount Policy Correction (Immediate, Zero-Cost)
**Finding**: 8 sub-categories with average margin rate below 8% (Paper, Binders,
Furnishings, Art, Storage, Labels, Accessories, Envelopes) account for 56.7% of order
volume but drive the majority of the company's $83,289 in discount-related profit erosion
— confirmed independently by SQL-based Pareto analysis and Random Forest feature importance.

**Action**: Implement a margin-rate floor in the discount approval workflow — orders on
sub-categories below the 8% margin threshold require managerial override to apply any
discount.

**Expected Impact**: Recovers up to 8.0% of total company profit ($83,289) with no change
to pricing, cost structure, or customer-facing operations.

**Owner**: Pricing/Revenue Operations team.

### 2. Real-Time Loss-Risk Flagging (1–2 Sprint Implementation)
**Finding**: A Random Forest classifier predicts order-level loss risk with AUC=0.977 and
94.1% recall on loss-making orders, using features available at order entry (category,
discount %, quantity, list/cost price).

**Action**: Embed the model as a pre-checkout risk score in the order/discount approval
system; route orders above a chosen risk threshold (e.g., >70% predicted loss probability)
to manual review before discount is applied.

**Expected Impact**: Extends the static policy in (1) to catch edge cases and new SKUs not
yet covered by fixed category rules, reducing residual loss leakage beyond the $83K estimate.

**Owner**: Data Science/Engineering, in coordination with Pricing Operations.

### 3. Segment-Specific Customer Retention (Next Quarter)
**Finding**: A high-value, low-satisfaction segment (6.4% of customers) spends 14.2x the
average but reports the lowest satisfaction score across all segments (3.3 vs 3.7)  — the
segment most exposed to churn-driven revenue loss given its outsized contribution.

**Action**: Prioritize this segment for proactive customer success outreach (dedicated
support channel, satisfaction follow-up post-purchase) ahead of broader retention campaigns.

**Expected Impact**: Directly protects the highest-concentration revenue segment; avoiding
churn in this group has disproportionately larger revenue impact than equivalent retention
spend on the two low-frequency segments (77.7% of the base, but far lower average spend).