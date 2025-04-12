class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        rangesList = []
        for r in ranges:
            rangesList = [*rangesList, *list(range(r[0], r[1]+1))]
        for i in range(left, right+1):
            if i not in rangesList:
                return False
        return True    
