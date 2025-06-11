class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        for i in range(n - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
