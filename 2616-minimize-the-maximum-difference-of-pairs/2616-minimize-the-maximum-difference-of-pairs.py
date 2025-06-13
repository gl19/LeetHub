class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        n = len(nums)
        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        while l <= r:
            mid = (l + r) // 2
            counter = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= mid:
                    counter += 1
                    i += 1

                i += 1
                
            if counter >= p:
                r = mid - 1
            else:
                l = mid + 1
                
        return l
            


        
        


