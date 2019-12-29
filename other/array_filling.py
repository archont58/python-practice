from random import randint

while True:
    a = input("Enter the length of array: ")
    try:
        a = int(a)
        break
    except ValueError:
        print("Enter number!")
        continue

m = []
for i in range(a):
    m.append(randint(1, 99))

for i in m:
    print(i, end=' ')

print()
