class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = max(nums)
        visited = [False] * (n + 1)
        for num in nums:
            if num <= 0:
                continue
            
            if num <= n:
                visited[num] = True
        
        for i in range(1, n + 1):
            if visited[i] == False:
                return i

        return max(1, max(nums) + 1)
