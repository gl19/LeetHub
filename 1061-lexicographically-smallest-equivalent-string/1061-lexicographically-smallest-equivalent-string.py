class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {}
        cache = {}

        for c1, c2 in zip(s1, s2):
            if c1 in d:
                d[c1].add(c2)
            else:
                d[c1] = set([c2])

            if c2 in d:
                d[c2].add(c1)
            else:
                d[c2] = set([c1])

        
        def dfs(cur, visited):
            visited.add(cur)
            smallest = cur
            for neighbor in d[cur]:
                if neighbor not in visited:
                    candidate = dfs(neighbor, visited)
                    if candidate < smallest:
                        smallest = candidate

            return smallest
        
        for c in d.keys():
            cache[c] = dfs(c, set())

        ret_str = ''
        for c in baseStr:
            if c in cache:
                ret_str += cache[c]
            else:
                ret_str += c

        return ret_str



            



        