class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_dict = Counter(nums2)                                             

    def add(self, index: int, val: int) -> None:
        self.nums2_dict[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_dict[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for i, val in enumerate(self.nums1):
            if tot - val in self.nums2_dict:
                ans += self.nums2_dict[tot - val]

        return ans

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)