def sum_str(num):
    num = str(num)
    sum_n = 0
    for i in range(len(num)):
        sum_n += int(num[i])
    return sum_n


while True:
    a = input("Enter the integer number: ")
    try:
        a = abs(int(a))
        break
    except ValueError:
        print("Enter the integer number!")
        continue

print("Sum of the numbers: ", sum_str(a))
