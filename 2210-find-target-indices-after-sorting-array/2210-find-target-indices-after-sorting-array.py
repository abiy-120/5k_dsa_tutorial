class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        answer = []
        index = -1
        try:
            index = nums.index(target)
        except:
            pass
        if index != -1:
            while index < len(nums) and nums[index] == target:
                answer.append(index)
                index += 1
        return answer