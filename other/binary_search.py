def binary_search(nums, item):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = nums[mid]
        if guess == item:
            return mid
        else:
            if guess < item:
                low = mid + 1
            else:
                high = mid - 1
    return None


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Index of the found element: ", binary_search(array, 2))
