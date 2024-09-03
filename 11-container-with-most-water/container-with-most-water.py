class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_area = 0

        while low < high:
            area = (high - low) * min(height[low], height[high])
            max_area = max(max_area, area)
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        
        return max_area