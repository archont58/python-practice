def fix_duplicates(array):
    res = []
    for i, v in enumerate(array):
        c = array[:i].count(v)
        if c:
            res.append(v + '_' + str(c))
        else:
            res.append(v)
    return res


chars = ["a", "b", "c", "a", "a", "d", "c", "a"]
print(fix_duplicates(chars))
