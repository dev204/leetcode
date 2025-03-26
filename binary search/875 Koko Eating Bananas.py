'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k.
Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas,
you may finish eating the pile but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours.

Input: piles = [1,4,3,2], h = 9
Output: 2
'''
# h = total num of hours av, k = banana eating speed
# key insight: h must be h >= len(p) since we can only eat from one pile per hour
# and the answer k wants to know min eating speed to eat all piles in exactly at least len(p) hours
# so ans has to be somewhere between 1 to max(piles) as this implies we can eat from each pile within 1 hr
# so we can search between 1 to max(piles) and first value that allows us to eat all piles will be output
# we can brute force for each value 1 to max(piles) and check which gives us tc O(max(piles) * len(piles))
# we can improve by implementing binary search instead of trying every value in range max(piles) which
# gives us tc of O( log (max(piles)) * len(piles))
# we can initialize range 1 to max(piles) with l and r pointers , apply BS find middle and count hours to eat all bananas,
# then move l and r pointers, search left if able to eat and right portion if not able to eat within h hours

def eatinghours(self, piles, bananaseaten):
    hours = 0
    for p in piles:
        hours += math.ceil(float(p) / bananaseaten)
    return hours


def minEatingSpeed(self, piles: List[int], hours: int) -> int:
    # answer will be between 1 and max pile
    l, r = 1, max(piles)
    # imp = l needs to start with one
    # otherwise we end up dividing by 0 as we keep
    # on decreasing
    minspeed = r
    while l <= r:
        bananaAmt = l + (r - l) // 2  # bananaAmt is the middle val
        eatingTime = self.eatinghours(piles, bananaAmt)
        if eatingTime > hours:
            # we need to increase speed so we try higher
            # num of bananas
            l = bananaAmt + 1
        else:
            minBanana = min(minspeed, bananaAmt)
            # we need to try with less bananas
            r = bananaAmt - 1
    return minBanana
