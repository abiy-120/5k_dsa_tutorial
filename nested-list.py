if __name__ == '__main__':
    l = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        l.append([name, score])
    scores.sort()
    secondLowestScore = list(set(scores))[1]
    lowestPeople = list(filter(lambda x: x[1] == secondLowestScore, l))
    lowestPeople.sort(key=(lambda x: x[0]))
    for i in lowestPeople:
        print(i[0])