class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDist = {}
        l, r = 0, 0
        res = 0

        while r < len(s):
            charDist[s[r]] = charDist.get(s[r], 0) + 1
            windowLen = r - l + 1
            replaced = windowLen - max(charDist.values())
            if replaced > k:
                charDist[s[l]] -= 1
                l += 1
                windowLen = r - l + 1

            res = max(windowLen, res)

            r += 1
            

        return res
            
        # l = 0
        # res = 0
        
        # for i in range(len(s)):
        #     count = 1
        #     currK = k
        #     for j in range(i+1, len(s)):
        #         if (s[i] == s[j]):
        #             count += 1
        #         elif currK != :
        #             currK -= 1
        #             count += 1
        #         else:
        #             break
        #     res = max(count, res)

        # return res