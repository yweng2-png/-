### Note on Cluster Count Selection

# Silhouette analysis shows k=2 yields the highest score (0.428), while k=4 through k=6
# cluster around 0.20-0.23 with no clear secondary peak -- indicating the customer base does
# not separate into sharply distinct groups, but rather forms a continuous spectrum across
# the selected features.
#
# k=2 was not selected despite its higher silhouette score because it would only separate
# customers along a single high-vs-low spending axis, offering limited actionable
# segmentation for targeted retention strategies. k=4 was selected as a pragmatic balance:
# it retains reasonable cluster cohesion (silhouette=0.226) while surfacing business-
# interpretable segments (e.g., differentiated by purchase frequency and spend level) that
# support differentiated marketing action -- a case where business interpretability was
# prioritized over marginal statistical optimality.
