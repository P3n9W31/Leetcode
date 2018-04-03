class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_start = 0
        cur_pro = 0
        max_pro = 0
        for index in range(1, len(prices)):
            if prices[index] < prices[index-1]:
                cur_pro = prices[index-1] - prices[min_start]
                min_start = index
                max_pro = max_pro + cur_pro
            if index == len(prices)-1:
                cur_pro = prices[index] - prices[min_start]
                max_pro = max_pro + cur_pro
            
        return max_pro