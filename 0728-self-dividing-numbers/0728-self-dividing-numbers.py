class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left,right+1):
            if self.isSelf(i):
                result.append(i)
        return result
    def isSelf(self,n):
        temp = n
        while(temp > 0):
            digit = temp % 10
            if digit == 0:
                return False
            if n % digit !=0:
                return False
            temp = temp // 10
        return True