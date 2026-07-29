class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        # res = nums[0]

        while r > l:
            m = (l+r)//2
            if nums[m] > nums[r]:
                # search right
                l = m + 1
            else:
                # search left
                r = m

        return nums[l]