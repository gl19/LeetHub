class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left_total = 0
        right_total = sum(nums)
        min_avg_diff_val = float('inf')
        min_avg_diff_idx = -1
        for i, num in enumerate(nums):
            left_total += num
            right_total -= num
            if n - i - 1 > 0:
                avg_diff = abs(left_total // (i + 1) - right_total // (n - i - 1))
            else:
                avg_diff = abs(left_total // (i + 1))

            if avg_diff < min_avg_diff_val:
                min_avg_diff_val = avg_diff
                min_avg_diff_idx = i

        return min_avg_diff_idx
            