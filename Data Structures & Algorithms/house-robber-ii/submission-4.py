class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i] = $ in ith house
        # no adjacent houses; 1st + last are neighbors
        # max $ rob

        # base case
        if len(nums) == 1:
            return nums[0]

        # first to second last
        dp1 = {}

        # second to last
        dp2 = {}

        # house = curr index
        # define the range for indexes to avoid adjacent houses
        def dfs(house, start, end):
            if end <= house:
                return 0

            if start == 0:

                if house in dp1:
                    return dp1[house]

                dp1[house] = max(nums[house] + dfs(house+2, start, end), dfs(house+1, start, end))

                return dp1[house]

            if start == 1:

                if house in dp2:
                    return dp2[house]

                dp2[house] = max(nums[house] + dfs(house+2, start, end), dfs(house+1, start, end))

                return dp2[house]
            
        return max(dfs(0, 0, len(nums)-1), dfs(1, 1, len(nums)))

            