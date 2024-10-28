# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        availablePot = 0
        m = len(flowerbed)
        if m < 2:
            maxBed = max(flowerbed)
            return n == 0 or maxBed != n 
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            availablePot += 1
        for i in range(1, m - 1):
            prevPot = flowerbed[i - 1]
            currPot = flowerbed[i]
            nextPot = flowerbed[i + 1]
            if prevPot == 0 and currPot == 0 and nextPot == 0:
                flowerbed[i] = 1
                availablePot += 1
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                availablePot += 1
        return availablePot >= n
