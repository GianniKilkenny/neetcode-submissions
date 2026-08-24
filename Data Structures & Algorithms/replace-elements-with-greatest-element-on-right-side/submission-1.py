class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1] * n
        max_so_far = -1
        for i in range(n - 1, -1, -1):
            res[i] = max_so_far    
            max_so_far = max(max_so_far, arr[i])
        return res
