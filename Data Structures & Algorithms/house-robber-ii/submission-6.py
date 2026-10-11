class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = {}
        dp2 = {}

        def dfs(house, firstRob: False):
            if firstRob and (house+1) >= len(nums):
                return 0
            elif (house) >= len(nums):
                return 0

            if firstRob:

                if house in dp1:
                    return dp1[house]
                    
                dp1[house] = max(nums[house] + dfs(house+2, firstRob), dfs(house+1, firstRob))

                return dp1[house]
            else:
                if house in dp2:
                    return dp2[house]

                dp2[house] = max(nums[house] + dfs(house+2, False), dfs(house+1, False))

                return dp2[house]

        return max(dfs(1, False), dfs(0, True))