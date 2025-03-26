'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Input: prices = [10,1,5,6,7,1]

Output: 6
'''

# keep 2 pointers at pos 0,1 sort of like sliding window
# if price l < price r, we calc profit
# otherwise if r <= l, we reset l to r
# we keep moving r fwd in both cases
# since we traverse the whole arr only once tc O(n) sc O(1)

def maxProfit(self, prices: List[int]) -> int:
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP