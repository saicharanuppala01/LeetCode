class Solution:
    def digitNumber(self, n: int) -> int:
        if n==0:
            return 0
        product = 1
        while n>0:
            product=product*(n%10)
            n=n//10
        return product
    def smallestNumber(self, n: int,t: int) -> int:
        while True:
            if self.digitNumber(n) % t == 0:
                return n
            n=n+1