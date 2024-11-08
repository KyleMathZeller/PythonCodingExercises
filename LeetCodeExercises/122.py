"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

 

Constraints:

    1 <= prices.length <= 3 * 104
    0 <= prices[i] <= 104

    I found the wording very strang on this problem, the idea of buying and selling on the same day is weird, it should never net you a profit. Therefore, I 
    assume it is basically premission to prevent issues if you algorithm "buys" on the last day, because you can just sell for net 0 profit. Considering it is lihe 121
    I think it is fair to assume the tweak to the solution is needed.

    For what ever reason thinking about the vallies on the previous problem and on this one it seemed like peaks were the important point so I worked in reverse.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestPriceSeen = prices[-1]
        previousPrice = prices[-1]
        maxProfit = 0
        for price in reversed(prices):
            if price > previousPrice:
                #We should never not want to sell on a peak therefore we will buy after everypeak even if to just sell
                maxProfit += highestPriceSeen - previousPrice
                highestPriceSeen = price
            previousPrice = price
        #this method is needed to catch if the "last"/first day is the cheapest
        #The reason this is okay is it always add the price to the profit however, 
        #if it triggers above highestPrice = prices[0] -> 0 = n - n
        if prices[0] == previousPrice:
            maxProfit += highestPriceSeen - prices[0]
                
        return maxProfit