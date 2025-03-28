'''
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

'''

# approach We can use a Max-Heap, which allows us to retrieve the maximum element in O(1) time. We initially insert all the weights into the Max-Heap, which takes O(logn) time per insertion. We then simulate the process until only one or no element remains in the Max-Heap. At each step, we pop two elements from the Max-Heap which takes O(logn) time. If they are equal, we do not insert anything back into the heap and continue. Otherwise, we insert the difference of the two elements back into the heap.

# Time complexity:  O(nlogn) Space complexity: O(n)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x,y = (heapq.heappop(stones)*-1),(heapq.heappop(stones)*-1)
            if x > y: # as first element will be bigger than second usually
                heapq.heappush(stones,(x-y)*-1)
        stones.append(0) # if stones is empty
        #return maxheap[0]*-1 if maxheap else 0
        return abs(stones[0])
