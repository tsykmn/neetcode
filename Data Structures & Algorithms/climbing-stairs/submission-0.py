class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [-1]*n

        def dfs(i):
            # valid
            if i == n:
                return 1

            # invalid
            if i > n:
                return 0

            # stored in arr, no repeated work
            if arr[i] != -1:
                return arr[i]

            arr[i] = dfs(i+1) + dfs(i+2)

            return arr[i]

        return dfs(0)

        

        