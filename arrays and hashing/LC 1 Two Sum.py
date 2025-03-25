'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Input:
nums = [3,4,5,6], target = 7

Output: [0,1]

'''
# TC O(n) SC O(n)


def twoSum(nums, target: int):
    d = collections.defaultdict(int)

    for i in range(len(nums)):
        if target - nums[i] in d:
            return [d[target - nums[i]], i]
        d[nums[i]] = i