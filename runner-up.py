if __name__ == '__main__':
    n = int(input())
    arr = list(set(list(map(int, input().split()))))
    arr.sort()
    print(arr[-2])
    