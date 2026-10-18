class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        left, right = 0, n
        res = 0

        for i in range(n):

            # odd length
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                right += 1
                left -= 1

            # even length
            left, right = i, i+1

            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                right += 1
                left -= 1

        return res