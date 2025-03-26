'''
Description
You are given an integer array heights where heights[i] represents the height of the bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]

Output: 36

'''

# since we want to maximise the amount of water, ww choose 2 pointers l and r and move the shorter pointer
# and calc area at every iteration until l = r

def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    area = 0

    while l < r:
        print(l, r)
        currArea = min(height[l], height[r]) * (r - l)
        area = max(area, currArea)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return area