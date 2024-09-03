class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_area = 0
        max_height = max(height)

        while low < high:
            area = (high - low) * min(height[low], height[high])
            max_area = max(max_area, area)

            if max_height * (high - low) < max_area:
                break
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        
        return max_area