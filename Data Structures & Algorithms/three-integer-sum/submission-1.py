class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1, n-1):
                if -(nums[i] + nums[j]) in nums[j+1:]:
                    s = sorted([nums[i], nums[j], -(nums[i] + nums[j])])
                    # print(s)
                    if s not in res:
                        res.append(s)

        return res
