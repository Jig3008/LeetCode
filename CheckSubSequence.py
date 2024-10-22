#Use Case: To Check whether any the given string is a subsequence of the parent or not

def checkSubString(childString, parentString):
  i = j = 0
  while i < len(childString) and j < len(parentString):
    if childString[i] == parentString[j]:
      i += 1

    j += 1

  return i == len(childString)    

result1= checkSubString('abc','abcde')
result2= checkSubString('abz','abcde')
(result1,result2)

#(True, False)
