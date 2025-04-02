def smallestEvenMultiple(n):
  for i in range(1, (n * 2) + 1):
      if i % 2 == 0 and i % n == 0:
          return i