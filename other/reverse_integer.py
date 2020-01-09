class Solution:
    def reverse(self, num):
        if num < 0:
            res = str(abs(num))
            res = res[::-1]
            res = int('-' + res)
        else:
            res = str(abs(num))
            res = int(res[::-1])
        return res if (2 ** 31 - 1) >= res >= -2 ** 31 else 0


result = Solution()
a = 590
b = 126372273825
print(result.reverse(a))
print(result.reverse(b))
