class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        lh = len(height)
        i, j = 0, lh - 1
        while i < j:
            distance = j - i
            lower = i if height[i] < height[j] else j
            area = height[lower] * distance
            if area > max_area:
                max_area = area
            if lower == i:
                i += 1
            else:
                j -= 1
        return max_area


sol = Solution()
test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# test = [1, 1]
print(sol.maxArea(test))
