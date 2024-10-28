# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# Example 1:

# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelsInString = []
        vowels = ['a','e','i','o','u']
        j = 0
        result = []
        for i in s:
            if i.lower() in vowels:
                vowelsInString.append(i)

        reversedVowelsInString = list(reversed(vowelsInString))

        for i in s:
            if i.lower() in vowels:
                result.append(reversedVowelsInString[0])
                reversedVowelsInString.pop(0)
            else:
                result.append(i)
            j += 1
        
        return ''.join(result)


