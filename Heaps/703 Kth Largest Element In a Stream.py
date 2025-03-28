'''
Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
'''

# We initialize a Min-Heap with the elements of the input array. When the add() function is called, we insert the new element into the heap. If the heap size exceeds k, we remove the smallest element (the root of the heap). Finally, the top element of the heap represents the k-th largest element and is returned.
import heapq
'''
Time Complexity:
O(m * log k)

- m is the number of times the add() function is called.
- Each add() call takes O(log k) time because it may insert or remove elements from a heap of size k.

Space Complexity:
O(k)

- The heap stores at most k elements at any time.
- So the space used is proportional to k.
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap,self.k = nums,k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]