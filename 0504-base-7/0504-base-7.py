class Solution:
    def convertToBase7(self, num: int) -> str:
        original = num
        stack=[]
        if num == 0:
            return "0"
        if num < 0:
            num=abs(num)
        while(num>0):
            remainder = num % 7
            stack.append(str(remainder))
            num = num // 7
        if original < 0:
            stack.append("-")
        return "".join(stack[::-1])