import itertools


class Solution:
    def consecutivelyLate(self, att: list[str]) -> bool:
        late_count = 0
        for day in att:
            if day == "L":
                late_count += 1
            else:
                late_count = 0
        if late_count >= 3:
            return True
        return False

    def checkA3s(self, n: int) -> int:
        records = 0
        cartesian_product = list(itertools.product(["A", "L", "P"], repeat=n))
        return len(cartesian_product)
        third_cp = int(len(cartesian_product) / 3)
        for comb in cartesian_product[:third_cp]:
            if comb.count("A") >= 2:
                records += 1
            elif self.consecutivelyLate(comb):
                continue
            else:
                continue
        return records

    def checkAs(self, n: int) -> int:
        records = 0
        cartesian_product = list(itertools.product(["A", "L", "P"], repeat=n))
        for comb in cartesian_product:
            if comb.count("A") >= 2:
                records += 1
            elif self.consecutivelyLate(comb):
                continue
            else:
                continue
        return records

    def consecutiveLs(self, n:int) -> int:
        if n <=2:
            return 0
        start = (2**(n-4))
        return int(start*(n-1))

    def checkRecord(self, n: int) -> int:
        records = 0
        for comb in itertools.product(["A", "L", "P"], repeat=n):
            if comb.count("A") >= 2:
                continue
            elif self.consecutivelyLate(comb):
                continue
            else:
                records += 1
        return records


sol = Solution()
for i in range(1, 14):
    print(f"{i} - {sol.checkAs(i)} - {sol.checkA3s(i)}")
    # print(f"{i} - {sol.consecutiveLs(i)}")
