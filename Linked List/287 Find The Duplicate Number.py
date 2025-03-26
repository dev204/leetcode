'''
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times.
Return the integer that appears more than once.

Input: nums = [1,2,3,2,2]

Output: 2

'''
# intuition : Think of each index as a node where value at each index points to the next node
# So i → nums[i], Because there is one duplicate, it creates a cycle in this graph, we can use Floyd's cycle det algo
# using slow and fast pointers. They must meet inside the cycle

# Step 2: Find Entry Point of Cycle
# Start a new pointer slow2 from 0, Move both slow2 and slow one step at a time
# They’ll meet at the start of the cycle, which is the duplicate number
# tc O(n) sc O(1)

def findDuplicate(self, nums: List[int]) -> int:
    # floyd's algorithm
    # take 2 pointers first, slow and fast, break when they meet for the first time
    slow = fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # from this point onwards, we take second slow pointer starting from zero
    # when they meet that's the duplicate number
    slow2 = 0
    while True:
        slow2 = nums[slow2]
        slow = nums[slow]
        if slow == slow2:
            return slow