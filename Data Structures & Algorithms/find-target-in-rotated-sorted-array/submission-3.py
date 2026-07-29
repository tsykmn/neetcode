class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r, l = len(nums)-1, 0
    
        while l <= r:
            m = (r+l)//2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                # left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1