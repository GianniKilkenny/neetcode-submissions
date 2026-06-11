class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        length = 0
        for n in nums:
            if n - 1 not in nums:
                while n + length in nums:
                    length += 1
            longest = max(length, longest)
            length = 0
        return longest