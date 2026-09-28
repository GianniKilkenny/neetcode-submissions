class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        m = 0
        for n in nums:
            if n == 1:
                current += 1
            else:
                m = max(current, m)
                current = 0
        return max(m, current)