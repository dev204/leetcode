'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

# O(n) space and time , can be achieved by calculating prefix and post fix in different arrays
# Can be improved by doing in O(1) space as well
# we can try to build the array somehow by traversing input twice

def productExceptSelf(self, nums: List[int]) -> List[int]:
    '''
    leftproduct = [1] * len(nums)
    for i in range(len (nums)):
        leftproduct[i] = (leftproduct[i-1] * nums[i]) if i != 0 else nums [i]
    rightproduct = [1] * len(nums)
    for i in reversed(range(len(nums))):
        rightproduct[i] = (rightproduct[i+1] * nums[i]) if i != len(nums)-1 else nums[i]
    ans = [1] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            ans[i] = rightproduct[i+1]
        elif i == len(nums) - 1:
            ans[i] = leftproduct[i-1]
        else:
            ans[i] = leftproduct[i-1] * rightproduct[i+1]
    '''
    # we can do in more optimal way with O(1) space
    prefix = 1
    res = [1] * len(nums)
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        print(i)
        res[i] *= postfix
        postfix *= nums[i]
    return res