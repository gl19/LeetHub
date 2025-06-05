class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {}
        cache = {}

        for c1, c2 in zip(s1, s2):
            if c1 in d:
                d[c1].add(c2)
            else:
                d[c1] = set([c1, c2])

            if c2 in d:
                d[c2].add(c1)
            else:
                d[c2] = set([c1, c2])

        
        def dfs(cur, visited, min_char):
            if cur in visited:   
                return

            visited.add(cur)
            has_visited_all = True
            for candidate in d[cur]:
                if candidate not in visited:
                    has_visited_all = False
                    dfs(candidate, visited.copy(), min(cur, candidate))

            if has_visited_all:
                for c in visited:
                    if c not in cache or min_char < cache[c]:
                        cache[c] = min_char
        
        for c in d.keys():
            dfs(c, set(), c)

        ret_str = ''
        for c in baseStr:
            if c in cache:
                ret_str += cache[c]
            else:
                ret_str += c

        return ret_str



            



        