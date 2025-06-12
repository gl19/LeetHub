class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        l = 0
        r = n - 1

        # binary search
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] >= newInterval[0]:
                r = mid - 1
            else:
                l = mid + 1

        # if prev overlaps
        i = l
        if l > 0 and intervals[l - 1][1] >= newInterval[0]:
            intervals[l - 1][1] = max(intervals[l - 1][1], newInterval[1])
            l -= 1
        else:
            intervals.insert(i, newInterval)
            i += 1
        
        while i < n and intervals[l][1] >= intervals[i][0]:
            intervals[l][1] = max(intervals[l][1], intervals[i][1])
            i += 1

        return intervals[:l + 1] + intervals[i:]
            



