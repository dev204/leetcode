'''
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting -> nlogn
        # heaps -> can be done through either min heap or max heap, solution below
        # quick select -> average time complexity O(n) and worst is O(n^2)
        # we choose a pivot (let's say right most), and partition the array into 2 halves in place
        # all elements less than pivot go into first half, all greater in second half, then we swap
        # pivot with starting of second half. at this point we know that all elements in first half will
        # be def smaller than pivot (but not necessarily sorted in 1st half) but still less than pivot
        # then we do the same process again on second half, take right most pivot and compare second half w pivot
        # O(n) avg case bcus every iteration we look at only one half the array, where we think target value will be
        # n operations to iterate thru all the array, n/2 op to iterate second half, n/4 similarly, assuming pivot is somewhere in the middle
        # n + n/2 + n/4 .... = this inifinite series evaluates to 2n -> O(n), in some cases pivot value
        # is always at the end of the array ie all elements are smaller than pivot, then we have to look into
        # all the elements except the last element as so on, hence worst case O(n^2) ie pivot is the greatest value
        k = len(nums) - k # this is the index we want in a sorted arr

        def quickSelect(l,r):
            pointer, pivot = l, nums[r]
            for i in range(l,r):
                # we compare every element nums[i] with pivot
                if nums[i] <= pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i] # if true then we swap with pointer
                    pointer += 1 # increment pivot
            # at this point all values on left of pointer are less than the pivot
            # now we swap right most number (pivot) with pointer
            nums[pointer],nums[r] = nums[r],nums[pointer]
            # now every value left of pivot is less, every value to right is more (but not necessary in sorted order within each side)

            #we now need to figure out which side of pivot does value kth largest lie
            # and then rescursively call for that half
            if k < pointer:
                return quickSelect(l,pointer-1)
            elif k > pointer:
                return quickSelect(pointer+1,r)
            else: # value found
                return nums[pointer]

        # now we just need to call our function
        return quickSelect(0,len(nums)-1)


        # above solution passes 41/42 cases and TLE one 1 case, but good to know quick select algorithm
        # max heap -> we push all elements to heap O(n) ,  then pop k times with each pop costing O(log n)
        # time complexity is O(n + k*log n) we leave this as time complexity bcus its not clear which is less - first part or second half
        # this is better than nlogn (sorting) bcus we can assume k will be smaller than n ie k << n

        # in min heap we build up the heap as we go and max elements will be k and never exceed k
        # when we limit to k, we will have k largest elements of the array in heap
        # among these k largest elements, and root will be the smallest and be the Kth largest elements
        # easy to visualise with small k value such as k = 2
        # after traversing full arr we will have 2 largest elements in heap
        # now if we need kth largest, it will be the root (smaller) element
        # O(Nlogk) (N operations on heap of size k)
        # Use Min Heap for efficiency, especially when n is large

        minheap = []

        for n in nums:
            heapq.heappush(minheap, n)

            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0]