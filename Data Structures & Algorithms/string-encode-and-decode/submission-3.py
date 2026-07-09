class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        if strs == []:
            return "None"

        for s in strs:
            strNum = len(s)
            res += str(strNum)
            res += '#'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        currWord = ""
        symb = False
        currNum = ""
        i = 0

        if s == "None":
            return res


        while i < len(s):
            if currNum == 0 and symb:
                symb = False
                res.append(currWord)
                currNum = ""
                currWord = ""

            if i < len(s):
                if (s[i].isnumeric() and not symb):
                    currNum += s[i]
                elif (s[i] == "#" and not symb):
                    symb = True
                    currNum = int(currNum)
                elif currNum != 0 and symb:
                    currWord += s[i]
                    currNum -= 1
            i += 1

        res.append(currWord)
        return res

            # if strNum != 0 and symb:
            #     currWord += s[i]
            #     strNum -= 1
            # elif strNum == 0 and symb:
            #     res.append(currWord)
            
            # if strNum == 0 and s[i].isnumeric():
            #     currWord = ""
            #     symb = False
            #     strNum = int(s[i])
            # elif strNum != 0 and s[i] == "#" and not symb:
            #     symb = True
