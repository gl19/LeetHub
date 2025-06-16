class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest_num = None
        max_diff = -1
        for num in nums:
            if smallest_num is None or smallest_num > num:
                smallest_num = num
            else:
                if num != smallest_num and num - smallest_num > max_diff:
                    max_diff = num - smallest_num
                
        return max_diff