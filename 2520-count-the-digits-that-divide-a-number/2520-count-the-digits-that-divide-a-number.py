class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while (num > 0):
            digit = num % 10
            if((temp % digit) == 0) and digit!=0:
                count = count + 1
            num = num // 10
        return count