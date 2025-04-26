class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            less = list(filter(lambda x: x  < i, nums))
            answer.append(len(less))
        return answer