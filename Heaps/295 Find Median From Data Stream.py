'''
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.

'''
# approach We initialize a Max-Heap and a Min-Heap. When adding an element, if the element is greater than the minimum element of the Min-Heap, we push it into the Min-Heap; otherwise, we push it into the Max-Heap. If the size difference between the two heaps becomes greater than one, we rebalance them by popping an element from the larger heap and pushing it into the smaller heap. This process ensures that the elements are evenly distributed between the two heaps, allowing us to retrieve the middle element or elements in O(1) time

# Time & Space Complexity Time complexity: O(m∗logn) for aaddNum(), O(m) for findMedian(). Space complexity: O ( n ) O(n)
# Where m m is the number of function calls and n n is the length of the array.

import heapq
class MedianFinder:

    def __init__(self):
        # we can use 2 arrays and keep them balanced, where all numbers in one arr should be <= num in secnd arr
        # the max number in small heap will always be less than min number in large heap
        # hence small = maxHeap, large = minHeap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # by default let's add to small arr
        heapq.heappush(self.small, num * -1)

        # max of small is less than or equal to min of small
        if (self.small and self.large and (self.small[0] * -1) > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # we check if the 2 arrs are balanced
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        return (self.small[0] * -1 + self.large[0]) / 2