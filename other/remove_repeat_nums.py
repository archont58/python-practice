old_list = [1, 5, 2, 1, 8, 8, 0]
new_list = []
[new_list.append(item) for item in old_list if item not in new_list]
print(new_list)
