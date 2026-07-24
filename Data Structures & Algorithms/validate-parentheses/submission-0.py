class Solution:
    def isValid(self, s: str) -> bool:
        dist = {')':'(', '}': '{', ']': '['}
        openLst = []

        # pseudocode
        # iterate for each chatacter in s
        # 2 conditions
        # if open bracket -> add to openLst
        # if closed bracket
        # one: do we have open bracket so far?
        # if not, False
        # two: check if same type as what we have in open
        # false 
        # remove openLst
        # return openLst == empty

        for i in range(len(s)):
            if s[i] in dist.values():
                openLst.append(s[i])

            if s[i] in dist and len(openLst) == 0:
                return False
            elif s[i] in dist and len(openLst) != 0:
                openBracket = openLst.pop()
                if dist[s[i]] != openBracket:
                    return False

        return len(openLst) == 0
        