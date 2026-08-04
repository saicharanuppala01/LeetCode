class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n=len(nums)
        ans=0
        nums.sort()
        for i in range(n-1):
            temp=abs(nums[i+1]-nums[i])
            if(temp>ans):
                ans=temp
        return ans