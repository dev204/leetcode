'''
Design a stack class that supports the push, pop, top, and getMin operations.
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.
'''

# using a var to keep track of min val won't work as we can pop that var and then we'll have calc again the min var
# use some DS ? take extra space
# we can maintain 2 stacks
# second stack will take in either - min(current value to be inserted, minimum value so far in main stack)
# this will keep track of min val so far in min stack and keep both stacks of the same size
# ie everytime we push, we push into both stacks, same for pop, we pop from both

# tc O(1) sc O(n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(val,self.minstack[-1]) if self.minstack else val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
