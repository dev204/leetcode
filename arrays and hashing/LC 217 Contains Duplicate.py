'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
'''
from typing import List
# TC O(n), SC O(n)

def containsDuplicate(nums: List[int]) -> bool:
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            return True
    return False

if __name__ == "__main__":
    print(containsDuplicate([1,2,3,44,44]))