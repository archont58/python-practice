def valid_parentheses(s):
    parentheses = {"(": ")", "[": "]", "{": "}"}
    open_par = {"(", "[", "{"}
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == parentheses[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []


a = "([)]"
print(valid_parentheses(a))
