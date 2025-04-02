if __name__ == '__main__':
  n = int(input().strip())
  if n % 2 != 0:
    print("Weird")
  else:
    if n > 20 or n in range(2, 6):
      print("Not Weird")
    elif n in range(6, 21):
      print("Weird")