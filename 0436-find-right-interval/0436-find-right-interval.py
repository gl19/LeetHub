class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start_idx = sorted([(start, i) for i, (start, end) in enumerate(intervals)])
        def binary_search(end):
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if start_idx[mid][0] < end:
                    l = mid + 1
                else:
                    r = mid

            return start_idx[l][1] if l < n else -1
        
        result = []
        for interval in intervals:
            result.append(binary_search(interval[1]))
        
        return result

