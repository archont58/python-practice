def common_factor(first, second):
    while first != 0 and second != 0:
        if first > second:
            first %= second
        else:
            second %= first

    divisor = first + second
    return divisor


one = 18
two = 12
print(common_factor(one, two))
