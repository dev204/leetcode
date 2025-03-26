'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times.
For example, the array nums = [1,2,3,4,5,6] might become:
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.
You may assume all elements in the sorted rotated array nums are unique,
A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Input: nums = [3,4,5,6,1,2], target = 1
Output: 4

'''

# array is divided into left sorted portion or right sorted portion
#     # we find middle element, then compare it to left most value
# if nums[l] <= nums[m]: then we are in left sorted portion of the array
# we can then check if target is within this range of values on left side l and middle, if so we search left side
# if not we search on right side
# else nums[l] > nums[m]: wer're in right sorted portion of the arr
# we again need to check if target is within range of r and middle, if so we search right if not we search left

# tc O(log n) sc O(1)
def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        print(l, r, m)
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:  # we are in left sorted portion of the array
            # more than the range of left portion, we search right
            if target > nums[m] or target < nums[l]:
                l = m + 1
            # search left
            else:
                r = m - 1
        # right portion
        else:
            if target > nums[r] or target < nums[m]:
                r = m - 1
            else:
                l = m + 1
    return -1