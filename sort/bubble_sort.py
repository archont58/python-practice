def bubble_sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True


random_nums = [3, 5, 2, 1, 7, 4]
print("List before sorting: ", random_nums)
bubble_sort(random_nums)
print("List after sorting: ", random_nums)

