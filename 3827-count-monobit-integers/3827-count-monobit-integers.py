class Solution:
    def countMonobit(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2

        limit = 1
        bits = 1
        while 2 * limit <= (n + 1):
            limit *= 2
            bits += 1

        return bits