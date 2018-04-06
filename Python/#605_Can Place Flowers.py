class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for index in range(1,len(flowerbed)-1):
            if flowerbed[index] != 1 and flowerbed[index-1] == 0 and flowerbed[index+1] == 0:
                count += 1
                flowerbed[index] = 1
        return count >= n