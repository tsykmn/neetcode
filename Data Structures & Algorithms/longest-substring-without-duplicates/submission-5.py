class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubstring = 0

        if s == "":
            return 0
            
        for char in range(len(s)):
            currS = set()
            currN = 0
            for i in range(len(s[char:])):
                if s[i+char] in currS:
                    break
                currS.add(s[i+char])
            
            maxSubstring = max(len(currS), maxSubstring)  

        maxSubstring = max(len(currS), maxSubstring)   

        return maxSubstring
        