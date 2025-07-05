class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        max_lucky = -1
        for key in count.keys():
            if key == count[key]:
                max_lucky = max(max_lucky, key)

        return max_lucky

