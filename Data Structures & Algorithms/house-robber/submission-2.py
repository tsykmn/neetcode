class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = {}
        def dfs(house):
            if len(nums) <= house:
                return 0
            
            if house in dp:
                return dp[house]

            dp[house] = max(nums[house] + dfs(house+2), dfs(house+1))

            return dp[house]

        return dfs(0)