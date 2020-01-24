class Solution:
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


nums_list = [2, 11, 10, 17, 13]
target_sum = 24
result = Solution()
print(result.twoSum(nums_list, target_sum))
