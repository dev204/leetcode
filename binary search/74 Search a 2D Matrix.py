'''
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

'''

# since martix is sorted is increasing order we can implement bs
# we can first search to find the row which can contain the target
# we find the middle row with l = top row and r = bottom row
# if target is more than last element of middle row we move l=mid + 1
# else target is in rows above middle we move r = mid - 1 ie we find this by comparing first element of middle row to target
# once we have the row we can implement simple bs to search target as individual rows are also sorted

# tc O(logn + logm) where m and n are matrix dimensions sc O(1)

class Solution:
    def binsearch(self,row,target):
        l,r = 0, len(row) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix) - 1
        mid = -1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        if mid == -1 : return False
        return self.binsearch(matrix[mid],target)