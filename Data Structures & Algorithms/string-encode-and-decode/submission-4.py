class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        # base case: if input empty, then no need to encode
        if strs == []:
            return "None"

        # add the length of the word and # to signal the start of the word
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
                # only convert currNum to int after symb to signal the start of the word
                # use symb in case # is included in the word
                
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
