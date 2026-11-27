class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)

        # Calculate the total reward for activating each item type:
        # 1 purchased copy + all free copies it provides.
        rewards = []

        for i in range(n):
            factor = items[i][0]
            free_count = 0

            for j in range(n):
                if i != j and items[j][0] % factor == 0:
                    free_count += 1

            rewards.append(free_count + 1)

        # dp[c] = maximum items obtainable with exactly c spending.
        NEG_INF = -10**9
        dp = [NEG_INF] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            price = items[i][1]
            reward = rewards[i]

            # States where this item type has been bought at least once.
            take = [NEG_INF] * (budget + 1)

            for cost in range(price, budget + 1):
                # First purchase: gain the activation reward.
                first_purchase = dp[cost - price] + reward

                # Additional purchase: gain only one purchased copy.
                extra_purchase = take[cost - price] + 1

                take[cost] = max(first_purchase, extra_purchase)

            # Either skip this item type or buy it.
            for cost in range(budget + 1):
                dp[cost] = max(dp[cost], take[cost])

        return max(dp)
