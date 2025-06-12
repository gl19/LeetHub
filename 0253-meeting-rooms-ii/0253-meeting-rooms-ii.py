class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort()

        num_rooms = 0
        max_rooms = 0
        heap = []
        for i in range(n):
            start, end = intervals[i][0], intervals[i][1]
            while len(heap) > 0 and heap[0] <= start:
                num_rooms -= 1
                heapq.heappop(heap)

            num_rooms += 1
            heapq.heappush(heap, end)

            if num_rooms > max_rooms:
                max_rooms = num_rooms

        return max_rooms

