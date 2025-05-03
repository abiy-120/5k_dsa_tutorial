class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1
        right = n -1
        index = (m + n) - 1
        while right >= 0:
            if nums1[left] <= nums2[right]:
                nums1[index] = nums2[right]
            else:
                nums1[index] = nums1[left]
                nums1[left] = nums2[right]
            right -= 1
            index -= 1
        nums1.sort()
