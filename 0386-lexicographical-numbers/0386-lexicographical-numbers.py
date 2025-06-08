class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        def dfs(num):
            if num > n:
                return

            ret.append(num)

            for i in range(10):
                dfs(num * 10 + i)

        for i in range(1, 10):
            dfs(i)

        return ret



            
