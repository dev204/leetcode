'''
Description
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5
'''

# approach - We start by calculating the frequency of each task and initialize a variable time to track the total processing time. The task frequencies are inserted into a Max-Heap. We also use a queue to store tasks along with the time they become available after the cooldown. At each step, if the Max-Heap is empty, we update time to match the next available task in the queue, covering idle time. Otherwise, we process the most frequent task from the heap, decrement its frequency, and if it's still valid, add it back to the queue with its next available time. If the task at the front of the queue becomes available, we pop it and reinsert it into the heap.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # better to process more freq char first to minimise total time taken
        # each task takes 1 unit of time
        # TC O(n) where n = num of tasks, SC = O(1) cus we have at most 26 chars
        count = Counter(tasks)  # we get map of char freq
        maxHeap = [-cnt for cnt in count.values()]  # we don't really care about chars just freq
        heapq.heapify(maxHeap)
        q = deque()  # double ended queue [count/freq, idletime/when task will be available next]
        time = 0
        while q or maxHeap:
            time += 1

            if maxHeap:
                # we pop most freq task and add 1 bcus of python implementation of maxHeap, normallly we subtract 1 as we will be processing the task and reducing freq
                freq = 1 + heapq.heappop(maxHeap)
                if freq:  # ie if freq not equal to 0 ie we haven't fully processed this task
                    q.append([freq, time + n])  # we add reduced freq and time when the task will be avail next

            if q and q[0][1] == time:  # if first element in q has the available time = current time, we can process it
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

# Time complexity: O(m)
# Space complexity: O(1) since we have at most  26 different characters.
# Where m is the number of tasks.
