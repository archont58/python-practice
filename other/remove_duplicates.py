def remove_duplicates(nums):
    i = 0
    while i < len(nums):
        if not nums:
            return 0
        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1


ar = [1, 2, 2, 3, 4, 6]
print(remove_duplicates(ar))
