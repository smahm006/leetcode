class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True
    def isAnagramBest(self, s: str, t: str) -> bool:
        count = [0] * 26
        lens = len(s)
        lent = len(t)
        if lens != lent:
            return False
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
            print(count)
        for i in count:
            if i != 0:
                return False
        return True
    

if __name__ == "__main__": 
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagramBest("anagram", "nagaram"))