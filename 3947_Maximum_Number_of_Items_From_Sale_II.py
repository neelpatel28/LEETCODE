class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        max_factor = max(factor for factor, price in items)

        freq = [0] * (max_factor + 1)

        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        total = freq[:]

        for f in range(1, max_factor + 1):
            for multiple in range(f * 2, max_factor + 1, f):
                total[f] += freq[multiple]

        items.sort(key=lambda x: x[1])

        ans = 0

        for factor, price in items:
            if price >= 2 * min_price:
                break

            gain = total[factor] - 1
            if gain <= 0:
                continue

            take = min(gain, budget // price)

            ans += 2 * take
            budget -= take * price

        ans += budget // min_price

        return ans
