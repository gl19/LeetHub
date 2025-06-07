class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            time1 = slots1[i]
            time2 = slots2[j]
            if min(time1[1], time2[1]) - max(time1[0], time2[0]) >= duration:
                return [max(time1[0], time2[0]), max(time1[0], time2[0]) + duration]

            if time1[1] > time2[1]:
                j += 1
            else:
                i += 1

        return []