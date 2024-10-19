# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution(object):
  def canConstruct(self, ransomNote, magazine):
      result = True
      magazineDict = {}
      for i in range(0, len(magazine)):
          if magazine[i] in magazineDict:
              magazineDict[magazine[i]] += 1
          else:
              magazineDict[magazine[i]] = 1
      for i in range(0, len(ransomNote)):
          if ransomNote[i] in magazineDict and magazineDict[ransomNote[i]] - 1 >= 0:
              magazineDict[ransomNote[i]] -= 1
          else:
              result = False
              break
      return result
