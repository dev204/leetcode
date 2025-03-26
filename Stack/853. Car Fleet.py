'''
There are n cars traveling to the same destination on a one-lane highway.
You are given two arrays of integers position and speed, both of length n.
position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.
A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.
A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
Return the number of different car fleets that will arrive at the destination.

Input: target = 10, position = [1,4], speed = [3,2]
Output: 1

'''

# speed = distance / time
# we can calc time for every car to reach the target using target-pos as dist
# we can sort based on position in DESC order of every car
# start traversin in reverse order and calc time for curr to reach target and append to a stack say timestack
# if current appended value is less or equal to value before it, we can "combine" it by popping the stack
# lastly num of car fleet will be eq to the len of the stack

# tc O(nlogn), sc O(n)
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the positions + speed arr in desc order
        # after first car, if second car reached faster than car before it, we can combine
        # it as 1 single fleet
        pair = [(p,s) for p,s in zip(position,speed)]
        print(pair)
        pair.sort(reverse=True)
        timestack = []

        for p,s in pair:
            timestack.append((target-p)/s) # decimal division
            if len(timestack) >= 2 and timestack[-1] <= timestack[-2]: #if latest car reaches before the one ahead of it
                timestack.pop()
        return len(timestack)