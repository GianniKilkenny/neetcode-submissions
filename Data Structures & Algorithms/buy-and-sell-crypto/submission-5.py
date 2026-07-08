class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mp = 0


        while r < len(prices):
            cur = prices[r] - prices[l]
            mp = max(cur, mp)
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            r += 1
        return mp

