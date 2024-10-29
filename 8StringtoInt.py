# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip() 
        if not s:
            return 0
        
        isNegative = False
        result = []
        
        start = 0
        if s[0] == '-':
            isNegative = True
            start = 1
        elif s[0] == '+':
            start = 1

        for i in range(start, len(s)):
            if s[i].isdigit():
                result.append(s[i])
            else:
                break
        
        if not result:
            return 0
        
        number = int("".join(result))
        
        if isNegative:
            number = -number
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if number < INT_MIN:
            return INT_MIN
        elif number > INT_MAX:
            return INT_MAX
        
        return number
