from collections import Counter
class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        rangesList = []
        for r in ranges:
            rangesList = [*rangesList, *list(range(r[0], r[1]+1))]
        for i in range(left, right+1):
            if i not in rangesList:
                return False
        return True    


def isSubset(a, b):
    for i in b:
        if i in a:
            a.remove(i)
        else:
            return False
    return True
y = isSubset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7])
def similarPairs(words: list[str]) -> int:
        words = [set(x) for x in words]
        count = 0
        for index, word in enumerate(words):
            count += words[index+1:].count(word)
        print(count, words)
        return count
z = similarPairs(["aabb","ab","ba"])