class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         s = numbers[i] + numbers[j]
        #         if s == target:
        #             return [i+1, j+1]

        # return [-1, -1]

        for i in range(n):
            l, r = i+1, n - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                if numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []