'''
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9

'''

# one way is to store in 2 arrays the max height for a position i starting from left and right
# left = [] will represent max height so far as seen from left side
# right = [] max ht from right side
# we can then calc trapped water by taking min(left[i],right[i] - height[i]

# we can save space as well and use 2 pointers
# idea is we keep track of leftMaxSoFar, rightMaxSoFar, for height i when we traverse from left to right we always know true leftMaxSoFar but not true rightMaxSoFar
# so in any case if leftMaxSoFar < rightMaxSoFar,then we can calc trapped water by leftMaxSoFar - height i
# and vice verca, water is always going to be trapped by min value so we only move min pointer
# O(n) tc, O(1)
def trap(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    lMaxSoFar, rMaxSoFar = height[l], height[r]
    res = 0

    while l < r:
        if lMaxSoFar < rMaxSoFar:
            # note- order of conditions is imp
            # we can't store any water on end points
            l += 1
            lMaxSoFar = max(lMaxSoFar, height[l])
            # we can't do res += min(lMaxSoFar,rMaxSoFar) - height[l]
            # as we don't know the true max right, we only know the max right so far
            # we want minimum of min(lMax,rMax) from O(n) solution
            # but if lMaxSoFar is already less than rMaxSoFar, we don't care about real value of rMaxSoFar
            res += lMaxSoFar - height[l]
        else:
            # and vice verca for r max
            r -= 1
            rMaxSoFar = max(rMaxSoFar, height[r])
            res += rMaxSoFar - height[r]
    return res