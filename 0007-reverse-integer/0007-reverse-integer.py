class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            sign = -1
        else:
            sign = 1
        num = abs(x)
        reversed_num=int(str(num)[::-1])
        ans = reversed_num * sign
        if (ans < -2**31) or (ans > 2**31-1):
            return 0
        return ans