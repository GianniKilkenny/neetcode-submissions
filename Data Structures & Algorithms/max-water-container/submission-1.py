class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1


        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            res = width * height

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            
            max_area = max(max_area, res)

            
        return max_area



            



