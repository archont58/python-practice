from random import randint

N = 5
numbers = []
for i in range(N):
    numbers.append(randint(0, 99))

print("Full list: ", numbers)

if numbers[0] > numbers[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if numbers[i] < numbers[min1]:
        a = min1
        min1 = i
        if numbers[a] < numbers[min2]:
            min2 = a
    elif numbers[i] < numbers[min2]:
        min2 = i

print("Two minimum values: ", numbers[min2], numbers[min1])
