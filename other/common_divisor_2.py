def common_factor2(m, n):
    a, b = 0, 1
    a1, b1, = 1, 0
    c, d = m, n
    while m > 0 and n > 0:
        q = c // d
        r = c % d
        if r == 0:
            break
        c, d, t, a1 = d, r, a1, a
        a = t - q*a
        t, b1 = b1, b
        b = t - q*b

    return d


one = 1769
two = 551
print(common_factor2(one, two))