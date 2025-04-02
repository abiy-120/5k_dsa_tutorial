def swap_case(s):
  result = ""
  for l in s:
      if l.islower():
          result += l.capitalize()
      else:
          result += l.casefold()
  return result