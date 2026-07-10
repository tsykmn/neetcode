class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sNum = set(nums)
        res = 0

        for currNum in sNum:
            streak = 0
            while currNum+streak in sNum:
                streak += 1
            res = max(streak, res)

        return res
        