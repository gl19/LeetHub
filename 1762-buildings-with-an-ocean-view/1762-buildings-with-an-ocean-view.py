class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ret = []
        max_val = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_val:
                ret.append(i)
                max_val = heights[i]

        ret.reverse()
        return ret
                