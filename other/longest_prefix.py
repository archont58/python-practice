def longest_prefix(array):
    if not array:
        return ""
    shortest = min(array, key=len)
    for i, ch in enumerate(shortest):
        for j in array:
            if j[i] != ch:
                return shortest[:i]
    return shortest


ar = ["flower", "flow", "flight"]
print(longest_prefix(ar))

