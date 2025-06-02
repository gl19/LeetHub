class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        lefts = [0 for _ in ratings]

        consec_increasing = 0
        for i in range(1, n):
            # If the current is higher than prev val increase consec increasing
            if ratings[i] > ratings[i - 1]:
                consec_increasing += 1
            else:
                consec_increasing = 0
               
            lefts[i] = consec_increasing

        rights = [0 for _ in ratings]
        consec_increasing = 0
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                consec_increasing += 1
            else:
                consec_increasing = 0
               
            rights[i] = consec_increasing

        return n + sum(max(l, r) for l, r in zip(lefts, rights))

            

