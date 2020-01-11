def insertion_sort(nums):
    # iteration starts from the second item because we assume the first item is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # saving a reference to the previous item
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # insert the item
        nums[j + 1] = item_to_insert


random_nums = [3, 5, 2, 1, 7, 4]
print("List before sorting: ", random_nums)
insertion_sort(random_nums)
print("List after sorting: ", random_nums)
