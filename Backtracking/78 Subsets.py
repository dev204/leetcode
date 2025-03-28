'''
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

# appreach We can use backtracking to generate all possible subsets. We iterate through the given array with an index i and an initially empty temporary list representing the current subset. We recursively process each index, adding the corresponding element to the current subset and continuing, which results in a subset that includes that element. Alternatively, we skip the element by not adding it to the subset and proceed to the next index, forming a subset without including that element.

# Time complexity: O(n * 2^n)
# Space complexity O(n) extra space. O(2^n) for the output list.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recurse(index, sub):
            '''
            Why current_subset.copy() is Needed:
In Python, lists are mutable objects, which means they are passed by reference. When you append current_subset to result, you’re actually appending a reference to the same list object. If you later modify current_subset (e.g., by backtracking with current_subset.pop()), the changes will affect all references to that list, including the ones already added to result.

By using current_subset.copy(), you create a new list that is a copy of current_subset at that moment. This ensures that the subset added to result remains unchanged, even if current_subset is modified
            '''
            # base case where index is indicating we have processed all nums elements
            if index == len(nums):
                res.append(sub.copy())
                return

            # choice 1 we add the current index
            sub.append(nums[index])
            recurse(index + 1, sub)

            sub.pop()  # backtracking

            # Choice 2 we simply move index forward and not include curr char
            recurse(index + 1, sub)

        recurse(0, [])
        return res