def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_array(arr[1:])


def max_num(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_num(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


a = [1, 2, 9, 4, 5]
print(sum_array(a))
print(max_num(a))

