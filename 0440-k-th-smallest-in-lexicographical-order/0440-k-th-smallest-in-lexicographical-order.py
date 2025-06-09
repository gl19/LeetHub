class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix, n):
            count = 0
            cur = prefix
            next_prefix = prefix + 1
            while cur <= n:
                count += min(n + 1, next_prefix) - cur
                cur *= 10
                next_prefix *= 10
            return count

        curr = 1
        k -= 1
        while k > 0:
            count = count_prefix(curr, n)
            if k >= count:
                k -= count
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr