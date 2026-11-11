class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        mn = min(need1, need2)
        mx = max(need1, need2)

        cost_separate = need1 * cost1 + need2 * cost2

        cost_mixed = (
            mn * costBoth
            + (need1 - mn) * cost1
            + (need2 - mn) * cost2
        )

        cost_combined = mx * costBoth

        return min(cost_separate, cost_mixed, cost_combined)
