class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 2 dictionaries
        # need tracks the count of characters needed for t
        # window counts the curr chars within the window frame
        need = Counter(t)
        window = {}

        # count characters we have found in window
        total_needed = len(need)
        total_window = 0

        # 2 pointers
        l = 0

        res = [-1, -1]
        res_count = float("inf")

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in need and window[s[r]] == need[s[r]]:
                total_window += 1

            # shrink window as long as it's valid

            while total_needed == total_window:
                curr_len = r-l+1
                if res_count > curr_len:
                    res = [l, r]
                    res_count = curr_len
                
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    total_window -= 1
                
                l += 1

        return s[res[0]:res[1]+1] if res_count != float("inf") else ""
            

        # if s == t:
        #     return s

        # # 2 pointers
        # l, r = 0, 0

        # # track which char from t we need to find
        # findChar = set()

        # # store final result
        # res = ""

        # while r < len(s):
        #     # same character
        #     # keep l same and move r to get the correct window len
        #     if s[r] in t:
        #         findChar.add(s[r])
        #         # avoid duplicates
        #         r+=1
        #         if len(findChar) == 1:
        #             while r < len(s) and (s[l] == s[r]):
        #                 l += 1
        #                 r += 1
        #     elif r != l:
        #         # not same character
        #         # continue moving r until we find every character in t
        #         r += 1
        #     else:
        #         r += 1
        #         l += 1

        #     if len(t) == len(findChar):
        #         window = s[l:r]
        #         if len(res) > len(window) or len(res) == 0:
        #             res = window
        #         l += 1
        #         r = l
        #         findChar = set()

        # return res
            
                
