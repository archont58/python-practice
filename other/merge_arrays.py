def merge_array(list_a, list_b):
    list_c = []

    size_a = len(list_a)
    size_b = len(list_b)

    i, j = 0, 0

    while i < size_a and j < size_b:
        if list_a[i] < list_b[j]:
            list_c.append(list_a[i])
            i += 1
        else:
            list_c.append(list_b[j])
            j += 1

    # Add last item to list
    if list_a[-1] < list_b[-1]:
        list_c.append(list_b[-1])
    else:
        list_c.append(list_a[-1])

    return list_c


list_1 = [1, 3, 4, 6, 9]
list_2 = [0, 2, 5, 7, 8]
print(merge_array(list_1, list_2))
