class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums.sort()

        left, right = 0, 0

        while left < len(nums):
            consecutiveNum = 1
            currI = left
            while right < len(nums):
                if (nums[currI]+1) == nums[right]:
                    consecutiveNum += 1
                    currI = right
                right += 1
            left += 1
            right = left + 1
            res = max(res, consecutiveNum)
            
        return res

        