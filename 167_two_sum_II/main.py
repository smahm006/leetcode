class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return [seen[diff]+1, i+1]
            else:
                seen[num] = i
        return []

sol = Solution()
test = {"numbers": [2,7,11,15], "target": 9}
print(sol.twoSum(**test))
