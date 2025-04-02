def isPalindrome(x):
  s = str(x)
  if s == s[::-1]:
      return True
  else:
      return False