class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit=n
        sum=0
        product=1
        while(n>0):
            rem=n%10
            sum=sum+rem
            product=product*rem
            n=n//10
        total=sum+product
        if((digit%total)==0):
            return True
        else:
            return False
