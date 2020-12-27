class Solution:
    def findComplement(self, num: int) -> int:
        nbase2 = bin(num)
        nbase2 = nbase2[2:]
        nbase2 = '0b' + nbase2.replace('0', '1')
        nmax = int(nbase2, 2)
        return nmax - num
        
"""
better solution
class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0: return 1
        t = num
        res = 0
        while t > 0:
            t = t >> 1
            res = res << 1
            res += 1
        return res ^ num
"""