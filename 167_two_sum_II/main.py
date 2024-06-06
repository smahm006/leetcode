class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]

    def twoSumNo2P(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return [seen[diff] + 1, i + 1]
            else:
                seen[num] = i
        return []


sol = Solution()
test = {"numbers": [2, 7, 11, 15], "target": 9}
print(sol.twoSum(**test))
