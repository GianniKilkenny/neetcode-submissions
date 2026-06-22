class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        i, j = 0, len(height) - 1
        max_l = height[i]
        max_r = height[j]

        while i < j:
            if max_l < max_r:
                i += 1
                max_l = max(max_l, height[i])
                water += max_l - height[i]
            else:
                j -= 1
                max_r = max(max_r, height[j])
                water += max_r - height[j]    
        return water         

