class Solution:
    def reverse(self, x: int) -> int:
        temp = 0
        sign = False
        if x < 0:
            sign = True
            x=abs(x)
        while x:
            temp, x = temp * 10 + x%10, x//10
        if 2**31 < temp or -(2**31) >= temp:
            return 0
        if sign == True:
            return -temp
        return temp
