class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        start, end = 0, (len(heights)-1)
        while (start < end):
            base = end - start
            max_area = base * min(heights[start], heights[end])
            if (max_area > res):
                res = max_area
            if (heights[start] < heights[end]):
                start += 1
            else: 
                end -= 1
        return res
            