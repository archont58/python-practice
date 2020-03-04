def searchInsert(nums, target):
    size = len(nums)
    for i in range(size):
        if nums[i] == target:
            return i
        elif target < nums[i]:
            return 0
        elif i < size - 1:
            if nums[i] < target < nums[i + 1]:
                return i + 1
        else:
            result = i + 1
    return result


a = [1, 3, 4, 6]
b = 7
print(searchInsert(a, b))


