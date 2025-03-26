'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

'''

# we can sort the arr first, then only check for negative numbers as 3 +ve numbers can't sum to 0
# check for 2 nums that sum up to the abs(-ve number) using 2 pointer, l=i+1,r=len(nums)-1
# increase l if sum < target, decrease r if sum > target
# O(n^2) tc, O(m) space for the output list Where m is the number of triplets
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []

    for i, a in enumerate(nums):
        if a > 0:
            break
        if i > 0 and nums[i - 1] == a:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threesum = a + nums[l] + nums[r]
            if threesum < 0:
                l += 1
            elif threesum > 0:
                r -= 1
            else:
                res.append((a, nums[l], nums[r]))
                l += 1
                r -= 1
                # for case [-2,0,0,2,2] where we want new l
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
