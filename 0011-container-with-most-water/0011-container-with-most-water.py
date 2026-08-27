class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left = 0
        right = n - 1
        ans=0
        while(left < right):
            temp_area = min(height[left],height[right]) * (right - left)
            ans = max(ans,temp_area)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return ans