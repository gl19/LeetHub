class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        has_deleted = False

        max_len = 0

        for i, num in enumerate(nums):
            if num == 0:
                # Check if we have already del one or not
                if has_deleted:
                    # If we already del we need to move left side of window
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else:
                    has_deleted = True

            cur_len = i - left + 1 - has_deleted
            # Only check if num is 1
            if cur_len > max_len:
                max_len = cur_len - (0 if has_deleted else 1)
        
        return max_len


            

