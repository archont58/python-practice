def removeElement(nums, val):
    for i in range(nums.count(val)):
        nums.remove(val)
    return nums


a = [0, 1, 2, 2, 3, 0, 4, 2]
v = 1
print(removeElement(a, v))
