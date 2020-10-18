# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
# and empty spaces .
#
# Example 1:
#
# Input: "1 + 1"
# Output: 2
# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23


def calculate(expression):
    answer = 0
    last_operator = '+'
    stack = []
    for char in expression:
        if char == " ":
            continue
        if char == '(':
            stack.append(answer)
            if last_operator:
                stack.append(last_operator)
            answer = 0
            continue
        if char in ['+', '-']:
            last_operator = char
            continue
        if char == ')':
            answer = calculate(str(answer) + stack[-1] + str(stack[-2]))
            stack = stack[:-2]
            continue
        answer = answer + int(char) if last_operator == '+' else answer - int(char)
    return answer


print(calculate('(1+(4+5+2)-3)+(6+8)'))