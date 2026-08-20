class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        right = 1
        max1 = 0
        ans = 0
        while(right<n):
            if(prices[left]<prices[right]):
                ans = prices[right] - prices[left]
                max1 = max(max1,ans)
            else:
                left=right
            right+=1
        return max1 
        