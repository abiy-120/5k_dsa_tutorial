class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        namesAndHeights = [[names[i], heights[i]] for i in range(len(names))]
        namesAndHeights.sort(key=lambda x: x[1], reverse=True)
        print(namesAndHeights)
        return [x[0] for x in namesAndHeights]
