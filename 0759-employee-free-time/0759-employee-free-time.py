"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        times = []
        for personal_schedule in schedule:
            for event in personal_schedule:
                times.append((event.start, event.end))

        times.sort()
        prev_end = times[0][1]
        free_times = []
        for time in times[1:]:
            if time[0] > prev_end:
                free_times.append(Interval(prev_end, time[0]))
            
            prev_end = max(prev_end, time[1])


        return free_times
        