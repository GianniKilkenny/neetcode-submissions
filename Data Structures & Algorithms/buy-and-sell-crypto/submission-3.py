class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        if not prices:
            return max_profit
        while r <= len(prices) - 1:
            cur = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            max_profit = max(cur, max_profit)
            r += 1
        return max_profit
