class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alt = 0
        max_alt = 0
        for v in gain:
            cur_alt += v
            if cur_alt > max_alt:
                max_alt = cur_alt

        return max_alt
