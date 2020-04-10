# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.


def maxProfit(self, prices: List[int]) -> int:
    
    max_diff =0
    
    for i, num in enumerate(prices):
        
        while i<(len(prices)-1):
            day_diff= prices[i+1]- num 

            if day_diff>0:
                max_diff+=day_diff
            
    return max_diff