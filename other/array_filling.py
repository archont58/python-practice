from random import randint

def array_filling(size):
    nums = []
    for i in range(size):
        nums.append(randint(1, 99))
    return nums

while True:
    length = input("Enter the length of array: ")
    try:
        length = int(length)
        break
    except ValueError:
        print("Enter the number!")
        continue

print(array_filling(length))
