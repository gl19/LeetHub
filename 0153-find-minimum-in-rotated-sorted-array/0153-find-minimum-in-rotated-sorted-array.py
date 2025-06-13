class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while right > left:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left] and nums[mid] < nums[right]:
                right = mid
            else:
                break
                
        return nums[0]