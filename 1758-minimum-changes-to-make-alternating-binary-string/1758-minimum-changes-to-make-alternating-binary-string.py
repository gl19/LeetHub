class Solution:
    def minOperations(self, s: str) -> int:
        # starting with 0
        is_zero_start_zero = True
        count_start_zero = 0

        is_zero_start_one = False
        count_start_one = 0
        for c in s:
            if (c == '0' and not is_zero_start_zero) or (c == '1' and is_zero_start_zero):
                count_start_zero += 1

            if (c == '0' and not is_zero_start_one) or (c == '1' and is_zero_start_one):
                count_start_one += 1

            is_zero_start_zero = not is_zero_start_zero
            is_zero_start_one = not is_zero_start_one

        return min(count_start_zero, count_start_one)
