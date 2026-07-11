class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        n = len(s)
        left, right = 0, n-1
        while (left != right) and left < n and right >= 0:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True