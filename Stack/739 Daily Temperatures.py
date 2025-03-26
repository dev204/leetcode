'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature
appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day,
set result[i] to 0 instead.

Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

'''
# find a way to keep track of temps encountered so far
# monotonic decreasing stack
# we initialize result as 0 * len (temp)
# we keep pushing to stack if colder temps are there
# as soon as we encounter a hot day than top of stack, we pop from stack until top of stack has a colder temp than current day
# we can push [tempVal, index] onto stack and when we pop, we calculate future day by subtracting indexes

# tc O(n) sc O(n)

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    st = []  # [temp,index]

    for idx, temp in enumerate(temperatures):
        while st and temp > st[-1][0]:
            t, i = st.pop()
            res[i] = idx - i
        st.append((temp, idx))
    return res