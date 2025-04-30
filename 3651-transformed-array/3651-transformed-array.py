class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [None] * size
        for i in range(size):
            if nums[i] == 0:
                result[i] = nums[i]
            elif nums[i] > 0:
                k = (i + nums[i]) % size
                result[i] = nums[k]
            else:
                k = (i - abs(nums[i])) % size
                result[i] = nums[k]
        return result