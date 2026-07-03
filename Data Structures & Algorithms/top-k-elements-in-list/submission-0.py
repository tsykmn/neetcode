class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elemLst = set()
        elemDist = {}
        for n in nums:
            if n not in elemLst:
                elemLst.add(n)
                elemDist[n] = nums.count(n)
        sortedDict = dict(sorted(elemDist.items(), key=lambda item: item[1], reverse=True))
        return list(sortedDict.keys())[:k]
