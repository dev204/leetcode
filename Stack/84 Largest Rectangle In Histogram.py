'''
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.
Note: This chart is known as a histogram.

Input: heights = [7,1,7,2,2,4]
Output: 8

'''
# monotonic increasing stack
# if the heights are in decreasing order we can't keep extending the reactangle, but we can extend if heights are equal or greater
# we need heights in increasing order, if they aren't we can remove the heights ie maybe we can use stack to do this
# in stack we can push [index, ht], keep pushing, if current < top of stack
# we calculate area by popping from stack, subtracting it's index from current index * height, and keep poppinp and repeating area calc until curr > stack top
# now when we push into stack, we put the index of curr as not it's curr index but the index of the last popped ht, as a
# small area can also be extended to the left
# we can be left with vals in our stack so we compute area similarly for these vals which can be extended to end of the stack
# as well all while keeping track of max area

# tc O(n) sc O(n)
def largestRectangleArea(self, heights: List[int]) -> int:
    maxArea = 0
    stack = []  # (index, height)

    for i, h in enumerate(heights):
        index = i
        while stack and stack[-1][1] > h:  # if curr ht is less than top of stack
            start, height = stack.pop()
            maxArea = max(maxArea, height * (i - start))
            # we also need to move starting point of curr height to last popped ht index
            index = start
        stack.append([index, h])

    # there can be elements left over, and these elements can be extended all the
    # way to the end of the heights as will be the case in mono increasing stack
    while stack:
        i, h = stack.pop()
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea
