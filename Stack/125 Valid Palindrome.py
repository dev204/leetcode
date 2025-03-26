''''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
Input: s = "([{}])"
Output: true
Input: s = "[(])"
Output: false
'''

# push char to stack if open braces, if close braces check if closing braces maps to same type of opening braces, return false otherwise
# return true if stack is empty
# tc O(n) sc O(n)
def isValid(self, s: str) -> bool:
    stack = []
    charmap = {']': '[', ')': '(', '}': '{'}
    for char in s:
        if char in charmap:
            if stack and stack[-1] == charmap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return len(stack) == 0