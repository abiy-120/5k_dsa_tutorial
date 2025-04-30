class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = ""
        for l in s:
            n += str(ord(l) % 96)
        i = 0
        while i < k:
            sum = 0
            for l in n:
                sum += int(l)
            n = str(sum)
            i += 1
        return int(n)