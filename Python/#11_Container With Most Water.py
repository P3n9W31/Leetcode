class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_cap = 0
        left = 0
        right = len(height) - 1
        while right > left:
                h = min(height[left], height[right])
                w = right - left
                cap = h*w
                if height[left] > height[right]:
                    right -= 1
                else:
                    left += 1
                if cap > max_cap:
                    max_cap = cap
        return max_cap