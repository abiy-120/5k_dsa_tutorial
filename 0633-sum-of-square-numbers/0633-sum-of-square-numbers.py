class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.floor(math.sqrt(c))
        while left <= right:
            power = left**2 + right**2
            if power == c:
                return True
            elif power > c:
                right -= 1
            else:
                left += 1
        return False