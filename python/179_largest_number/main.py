'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
'''

class CompareStrNum(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def weigh(self, num: str) -> float:
        weight = float(num[0])
        for i in range(1, len(num)):
            weight += (int(num[i])-int(num[i-1]))/10**i
        return weight    
    def largestNumber(self, nums: list[int]) -> str:
        if all(num == 0 for num in nums):
            return "0"
        snums: list[str] = list(map(str, nums))
        snums_weighted = list(map(self.weigh, snums))
        snums_weighted = sorted(range(len(snums_weighted)),key=snums_weighted.__getitem__, reverse=True)
        snums_weighted = [snums[x] for x in snums_weighted]
        # error checking
        ln = [snums_weighted[0]]
        for i in range(1, len(snums_weighted)):
            ln_snw = ln[i-1] + snums_weighted[i]
            snw_ln = snums_weighted[i] + ln[i-1]
            check = int(ln_snw) > int(snw_ln)
            if check:
                ln.append(snums_weighted[i])
            else:
                ln.insert(i-1, snums_weighted[i])
        return "".join(ln)
    def largestNumberBest(self, nums: list[int]) -> str:
        snums = list(map(str, nums))
        snums.sort(key=CompareStrNum)
        return "".join(snums)
            
if __name__ == "__main__": 
    import random
    sol = Solution()
    test = [random.randint(0, 1000000) for _ in range(1000000)]
    sol.largestNumber(test)

