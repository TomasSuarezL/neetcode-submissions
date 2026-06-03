class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_dif = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                dif = prices[j] - prices[i]
                if (dif > max_dif):
                    max_dif = dif
        return max_dif