'''
You are given an array of length n which was originally sorted in ascending order.
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
Input: nums = [3,4,5,6,1,2]
Output: 1

'''


def findMin(self, nums: List[int]) -> int:
    # one way is to find the pivot which can be O(n)
    # array is divided into left sorted portion or right sorted portion
    # we find middle element, then compare it to left most value
    # if greater or equal than left, that means middle is part of
    # left sorted portion (we need equal for edge case where middle is left value also) and we search right side
    # else we're in right sorted position that means all values to the right are going to be greater and we search left

    # tc O(log n) sc O(1)
    l, r = 0, len(nums) - 1
    minval = nums[0]
    while l <= r:
        if nums[l] < nums[r]:
            minval = min(minval, nums[l])
            break
        m = l + (r - l) // 2
        minval = min(minval, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return minval