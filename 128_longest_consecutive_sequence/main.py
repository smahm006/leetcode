class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max = 0
        maxes = []
        print(nums)
        for i in range(1, len(nums)):
            print(nums[i], nums[i-1], nums[i] - nums[i-1])
            if nums[i]  == nums[i-1]:
                continue
            elif nums[i] - nums[i-1] in [0, 1]:
                max += 1
            else:
                maxes.append(max)
                max = 0
        maxes.append(max)
        return sorted(maxes)[-1] + 1

sol = Solution()
test = [0, 1, 1, 2]
print(sol.longestConsecutive(test))
