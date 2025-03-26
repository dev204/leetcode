'''
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''
from typing import List

'''
You need to explore many possible combinations (the decision tree).
At each decision point, you can add either '(' or ') (based on rules).
After trying a path, you go back (backtrack) and try another option.
'''
# we can use backtracking here to append first open brace, while tracking count of open < n and then close while close < n
# then we can pop and backtrack , this is like a dfs sol

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combination = []

        def recursiveGP(left,right):
            # Base case: stop when the combination is complete
            if left == right == n:
                res.append("".join(combination))
                return
            # Try adding "("
            if left < n:
                combination.append("(")
                recursiveGP(left + 1, right)
                combination.pop() # Backtrack: remove the last character
            # Try adding ")"
            if right < n and right < left:
                combination.append(")")
                recursiveGP(left,right + 1)
                combination.pop() # Backtrack: remove the last character
        recursiveGP(0,0)
        return(res)