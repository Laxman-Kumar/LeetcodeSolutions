def myPow(x: float, n: int) -> float:
        if n < 0:
            return 1 / myPow(x, abs(n))
        ans = 1
        while n:
            if n & 1:
                ans *= x
            n >>= 1
            x *= x
            
        return ans

print(myPow(4,9))
