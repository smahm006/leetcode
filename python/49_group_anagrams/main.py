class Solution:
    def sum_octals(self, word: str):
        total = 0
        for s in word:
            total += ord(s)
        return str(total) + "".join(sorted(word))

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        ordstrs = map(self.sum_octals, strs)
        for i, ordinal in enumerate(ordstrs):
            if ordinal in groups:
                groups[ordinal].append(strs[i])
            else:
                groups[ordinal] = [strs[i]]
        res = list(groups.values())
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams([""]))
    print(sol.groupAnagrams(["", "b", ""]))
    print(sol.groupAnagrams(["hhhhu", "tttti", "tttit", "hhhuh", "hhuhh", "tittt"]))
    print(sol.groupAnagrams(["ill", "duh", "rig", "rig", "hay", "hay"]))
