class Solution:
    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in nums:
                first = nums.index(num)
                second = nums.index(n)
                break
        return first, second


nums_list = [2, 13, 10, 17, 1]
target_sum = 14
result = Solution()
print(result.twoSum(nums_list, target_sum))
