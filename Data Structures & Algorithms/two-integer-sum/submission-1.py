class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #diff = target - nums[i]

    # need index and values

        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[nums[i]] = i