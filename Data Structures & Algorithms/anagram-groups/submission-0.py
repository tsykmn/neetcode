class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dist = {}
        for s in strs:
            # print(s)
            lstSort = sorted(s)
            wordSort = "".join(lstSort)
            if wordSort not in dist.keys():
                dist[wordSort] = [s]
            else:
                lst = dist.get(wordSort)
                lst.append(s)
                dist[wordSort] = lst
        return list(dist.values())