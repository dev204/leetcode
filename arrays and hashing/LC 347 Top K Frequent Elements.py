import collections
from typing import List
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

'''

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # we need to use min heap and limit it to size k
    # we need to discard elements with min frequence at the top

    # TC O(nlogk) as heap size is always k
    # SC O(n+k) O(n) for frequency map + O(k) for the heap = O(n + k)

    d = collections.defaultdict(int)
    for n in nums:
        d[n] += 1
    import heapq
    minheap = []

    for n in d.keys():
        heapq.heappush(minheap, (d[n], n))
        if len(minheap) > k:
            heapq.heappop(minheap)
    ans = []
    for i in range(k):
        ans.append(heapq.heappop(minheap)[1])
    return ans

# bucket sort
# O(n) space and time
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # we store count or element Freq array -> list of elements mapping
    # 3 -> [1], 2 -> [2], 3 -> [3]
    # this list of count/freq array is bounded by size of the input arr, ie max times an element can occur is len(arr) and we traverse from the end
    # hence worst case O(n) to iterate through count array to get the list at that count
    # and then O(n) once again (worst time) to get the elements from the list
    # = O(n+n = 2n) = O(n) time complexity
    # memory O(n) for hashmap
    d = {}

    for n in nums:
        d[n] = 1 + d.get(n, 0)

    freq = [[] for i in range(len(nums) + 1)]  # we need +1 as 0 doesn't make sense but freq could be len(nums) + 1

    for num, count in d.items():
        freq[count].append(num)

    res = []
    # traverse in reverse as high freq
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res