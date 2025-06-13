class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_len = 0

        for num in set_nums:
            if num - 1 in set_nums:
                continue

            counter = 1
            while num + 1 in set_nums:
                num += 1
                counter += 1

            if counter > max_len:
                max_len = counter

        return max_len
