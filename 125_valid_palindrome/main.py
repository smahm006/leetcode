import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, k = 0, len(s) - 1
        while i < k:
            # print(f"{i}: {s[i]}\n{k}: {s[k]}\n")
            if not s[i].isalnum():
                i += 1
                continue
            elif not s[k].isalnum():
                k -= 1
                continue
            if s[i].casefold() != s[k].casefold():
                return False
            i += 1
            k -= 1
        return True

    def isPalindromeNo2P(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        return s == s[::-1]


sol = Solution()
test = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(test))
