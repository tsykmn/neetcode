class Solution:

    def encode(self, strs: List[str]) -> str:
        # base case
        # if list empty, just return None
        if strs == []:
            return "None"

        # for each word, compute length and # (mark as start of the word)
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i]))
            res += "#"
            res += strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left, right = 0, 0
        symb = False
        numWord = 0

        if s == "None":
            return res

        while left <= right and right < len(s):
            if s[right].isnumeric() and not symb:
                right += 1
            elif s[right] == "#":
                symb = True
                numWord = int(s[left:right])
                right += 1
            
            if symb:
                res.append(s[right:numWord+right])
                right = numWord+right
                left = right
                right += 1
                symb = False

        return res


