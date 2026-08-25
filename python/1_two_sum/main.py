class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indeces = []
        for i in range(len(nums)):
            diff = target - nums[i]
            nnums = nums[i + 1 :]
            if diff in nnums:
                index = nums.index(diff, i + 1)
                indeces.append(i)
                indeces.append(index)
                break
        return indeces

    def twoSumLR(self, nums: list[int], target: int):
        nums.sort()
        lptr = 0
        rptr = -1
        for _ in range(len(nums)):
            print(nums[lptr] + nums[rptr])
            if nums[lptr] + nums[rptr] < target:
                lptr += 1
            elif nums[lptr] + nums[rptr] > target:
                rptr -= 1
            else:
                print(lptr, rptr)
                return [lptr, len(nums) + rptr]
        return []

    def twoSumBest(self, nums: list[int], target: int):
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[num] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSumBest([3, 2, 4, 9], 6))
    print(sol.twoSumBest([3, 3], 6))
    print(sol.twoSumBest([2, 5, 5, 11], 7))
