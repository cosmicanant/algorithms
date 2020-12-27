class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ct = 0
        l = len(flowerbed)
        prevIndex = -2
        for i in range(l):
            num = flowerbed[i]
            if num == 0 and (i - prevIndex  == 2) and ( ( i+1 < l and flowerbed[i+1] == 0) or i == l - 1) :
                prevIndex = i
                ct += 1
            if(num == 1):
                prevIndex = i
        return ct == n
                
if __name__ == "__main__":
    p = Solution().canPlaceFlowers(
        [1,0,0,0,1,0,0],
        2
    )
    print(p)