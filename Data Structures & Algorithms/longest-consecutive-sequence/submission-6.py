class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set(nums)
        count = 0
        max_count = float("-inf")

        if not nums:
            return 0
        for n in nums:
            if n - 1 not in nums:
                count += 1
                while n + count in nums:
                    count += 1
            max_count = max(max_count, count)
            count = 0
        return max_count


