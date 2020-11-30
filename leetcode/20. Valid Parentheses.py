class Solution:
    def isValid(self, s: str) -> bool:
        t = ''
        valid = ['()','{}','[]']
        for i in range(len(s)):
            t += s[i]
            if i%2==1:
                print("1 - ",t)
                print("2 - ",valid[i])
                if t == valid[i]:
                    return True
        else:
            return False
