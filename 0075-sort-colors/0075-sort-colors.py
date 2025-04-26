class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min = nums[i]
            for j in range(i, len(nums)):
                if nums[j] < min:
                    min = nums[j]
                    nums[j] = nums[i]
                    nums[i] = min
        