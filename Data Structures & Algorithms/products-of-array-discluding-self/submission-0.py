class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            exceptSelf = nums[:i] + nums[i+1:]
            total = math.prod(exceptSelf)
            res.append(total)

        return res
        