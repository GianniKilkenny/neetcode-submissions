class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        #key = number: value = count
        for key in count:
            if count[key] > len(nums) / 2:
                return key
        