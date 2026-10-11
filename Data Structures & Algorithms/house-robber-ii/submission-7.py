class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        dp =[{}, {}]

        def dfs(house, firstRob):
            if house >= len(nums) or ((firstRob == 0) and house >= len(nums) - 1):
                return 0

            if house in dp[firstRob]:
                return dp[firstRob][house]
            
            dp[firstRob][house] = max(nums[house] + dfs(house+2, firstRob), dfs(house+1, firstRob))

            return dp[firstRob][house]

        return max(dfs(0, 0), dfs(1, 1))

            
        