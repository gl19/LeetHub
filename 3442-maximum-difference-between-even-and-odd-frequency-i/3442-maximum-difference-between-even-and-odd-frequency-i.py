class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        max_odd = 0
        min_even = float('inf')
        for count in counts.values():
            if count % 2 == 0:                
                if count < min_even:
                    min_even = count
            else:
                if count > max_odd:
                    max_odd = count
        
        return max_odd - min_even
