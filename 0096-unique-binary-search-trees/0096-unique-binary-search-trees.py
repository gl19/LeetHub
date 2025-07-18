class Solution:
    def numTrees(self, n: int) -> int:
        dp = defaultdict(int)
        def helper(left, right):
            nonlocal dp
            if left >= right:
                return 1
            
            difference = right - left
            if difference in dp:
                return dp[difference]

            total_trees = 0
            for i in range(left, right + 1):
                left_trees = helper(left, i - 1)
                right_trees = helper(i + 1, right)
                total_trees += left_trees * right_trees

            dp[difference] = total_trees

            return total_trees

        return helper(1, n)
        

