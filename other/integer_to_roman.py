def integer_to_roman(num):
    romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ""
    for i, j in enumerate(nums):
        while num >= j:
            result += romans[i]
            num -= j
        if num == 0:
            return result

    return result


_int = 53
print(integer_to_roman(_int))
