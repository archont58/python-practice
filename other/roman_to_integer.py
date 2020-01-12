def roman_to_integer(num):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    result = 0
    for i in num[::-1]:
        current = romans[i]
        if prev > current:
            result -= current
        else:
            result += current
        prev = current
    return result


roman = "MCMXCIV"
print(roman_to_integer(roman))
