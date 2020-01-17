def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

    return nums


unsorted_nums = [9, 3, 5, 2, 1, 7, 4, 1]
print("List before sorting: ", unsorted_nums)
selection_sort(unsorted_nums)
print("List after sorting: ", unsorted_nums)
