# Least Number of Unique Integers after K Removals
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        initialDict = {}
        for num in arr:
            if num in initialDict:
                initialDict[num] += 1
            else:
                initialDict[num] = 1
        sorted_by_values_asc = sorted(initialDict.items(), key=lambda item: item[1])

        for num, count in sorted_by_values_asc:
            if k >= count:
                k -= count
                initialDict.pop(num)
            else:
                break
        return len(initialDict)
      
