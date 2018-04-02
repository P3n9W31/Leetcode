class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_pro = 0
        for price in prices:
            min_price = min(price, min_price)
            cur_pro = price - min_price
            max_pro = max(cur_pro, max_pro)
        return max_pro
            