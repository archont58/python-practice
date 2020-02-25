def maxSubArray(nums):
    size = len(nums)
    result = nums[0]
    sum = 0
    min_sum = 0
    for i in range(size):
        sum += nums[i]
        result = max(result, sum - min_sum)
        min_sum = min(min_sum, sum)
    return result


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(a))
