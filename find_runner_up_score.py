if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    l = [i for i in arr]
    l.sort()
    print(l[-(l.count(l[-1]) + 1)])
