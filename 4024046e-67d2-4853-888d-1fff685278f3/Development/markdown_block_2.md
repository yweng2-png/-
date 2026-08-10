### Critical Note: Why AUC Reaches Near-Perfect Levels

The interpretable model (using Margin_Rate) achieves AUC=1.000. This is not an artifact of
overfitting or data leakage in the conventional sense — it reflects the underlying business
logic: since `Profit = Quantity × [List_Price × (1 - Discount%) − Cost_Price]`, and Quantity
is always positive, the sign of Profit is a **deterministic function** of Margin_Rate and
Discount_Percent (Profit < 0 ⟺ Margin_Rate < Discount_Percent / 100).

This means the "prediction" task is closer to a business rule than a genuine machine
learning problem — a simple rule engine (flag any order where Margin_Rate < Discount%)
would achieve equivalent accuracy with zero training cost. 

**The value of the RandomForest model here is not predictive novelty, but operational
packaging**: it (1) generalizes cleanly to new Sub_Categories not explicitly hard-coded
into a rules engine, (2) quantifies risk as a probability score rather than a binary flag,
enabling risk-tiered discount approval thresholds, and (3) surfaces the underlying business
rule automatically from data, which is useful when the rule itself isn't yet known (e.g.,
across a much larger, less well-understood SKU catalog).