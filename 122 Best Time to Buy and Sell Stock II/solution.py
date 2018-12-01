class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        max_profit = 0
        i = 0
        while i < length - 1:
            while i < length - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < length - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
         
            max_profit += (peak - valley)
        return max_profit
