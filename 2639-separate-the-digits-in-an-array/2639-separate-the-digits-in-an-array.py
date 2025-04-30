class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            for d in str(num):
                answer.append(int(d))
        return answer