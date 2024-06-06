class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        lenums = len(nums)
        triplets = []
        nums.sort()
        print(nums)
        for i in range(1, lenums):
            sum = nums[i] + nums[i-1]
            print(f"{nums[i-1]} + {nums[i]} == {sum}")
            if -sum in nums[i+1:] or -sum in nums[:i-1]:
                res = [nums[i], nums[i-1], -sum]
                triplets.append(tuple(sorted(res)))
            elif nums[i] != 0 and -nums[i] in nums[:i] and 0 in nums[:i]:
                res = [nums[i], -nums[i], 0]
                triplets.append(tuple(sorted(res)))
        triplets = (set(triplets))
        return [list(triplet) for triplet in triplets]
