'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5
'''
# we keep pushing to stack if number, if NaN we pop last two elements and apply the operation and push res back onto stack
# i'll have to make sure the order is correct in case of - and /
# tc O(n) sc O(n)

def evalRPN(self, tokens: List[str]) -> int:
    s = []
    for t in tokens:
        if t == '+':
            s.append(s.pop() + s.pop())
        elif t == '-':
            a, b = s.pop(), s.pop()
            s.append(b - a)
        elif t == '*':
            s.append(s.pop() * s.pop())
        elif t == '/':
            a, b = s.pop(), s.pop()
            s.append(int(b / a))
        else:
            s.append(int(t))
    return s.pop()