'''
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Input:
nums = [2,5,6,9]
target = 9
Output: [[2,2,5],[9]]

'''
# We can use backtracking to recursively traverse these paths and make decisions to choose an element at each step. We maintain a variable sum, which represents the sum of all the elements chosen in the current path. We stop this recursive path if sum == target, and add a copy of the chosen elements to the result.
# We recursively traverse the array starting from index i. At each step, we select an element from i to the end of the array. We extend the recursive path with elements where sum <= target after including that element. This creates multiple recursive paths, and we append the current list to the result whenever the base condition is met.

# In the worst case, the algorithm explores all possible subsets of the input list `nums`. If there are `n` elements in `nums`, the number of possible combinations can be up to `2^n`, leading to a time complexity of O(2^n). However, since we also have to consider the number of valid combinations that sum to the target, the effective time complexity can be influenced by the specific values in `nums` and the target.
# The space complexity is determined by the space used for the recursion stack and the storage of the results. The maximum depth of the recursion stack can go up to `n` in the worst case, leading to a space complexity of O(n). Additionally, the space required to store the results in `res` depends on the number of valid combinations found, which can also contribute to the overall space complexity. Therefore, the overall space complexity can be considered O(n + k), where `k` is the number of valid combinations stored in `res`.
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res