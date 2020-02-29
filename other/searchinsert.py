def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


a = [1, 3, 4, 6, 9]
b = 5
print(searchInsert(a, b))
