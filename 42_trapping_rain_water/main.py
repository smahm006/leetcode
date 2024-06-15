class Solution:
    def trap(self, height: list[int]) -> int:
        lh = len(height)
        total_area = 0
        i = 0
        stop = 0
        while i < lh:
            area = 0
            j = i + 1
            if i == lh - 1:
                break
            if height[i] == 0:
                i += 1
                continue
            while height[i] > height[j] and j != lh - 1:
                j += 1
            if j == lh - 1:
                stop = i
                break
            elif j - i != 1:
                distance = j - i - 1
                lower = height[i] if height[i] < height[j] else height[j]
                blacks = sum(height[i + 1 : j])
                area = (distance * lower) - blacks
                total_area += area
                i = j - 1
            else:
                i += 1
        i = lh - 1
        while i > stop:
            area = 0
            j = i - 1
            if i == stop:
                break
            if height[i] == 0:
                i -= 1
                continue
            while height[i] > height[j] and j != stop:
                j -= 1
            if i - j != 1:
                distance = i - j - 1
                lower = height[i] if height[i] < height[j] else height[j]
                blacks = sum(height[j + 1 : i])
                area = (distance * lower) - blacks
                total_area += area
                i = j + 1
            elif j == stop:
                break
            else:
                i -= 1
        return total_area


sol = Solution()
# test = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# test = [4, 2, 0, 3, 2, 5]
# test = [4, 2, 3]
# test = [5, 4, 1, 2]
test = [9, 8, 2, 6]
# test = [1, 7, 5]
print(sol.trap(test))
