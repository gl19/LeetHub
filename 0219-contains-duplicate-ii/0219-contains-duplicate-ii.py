class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_pos = defaultdict(int)
        for i, num in enumerate(nums):
            if num in num_pos and i - num_pos[num] <= k:
                return True

            num_pos[num] = i

        return False
