class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        longest = 0
        for i in range(n):
            d = defaultdict(int)
            for j in range(i, n):
                d[s[j]] += 1
                vals = list(d.values())
                flag = False
                for k in range(1, len(vals)):
                    if vals[k - 1] != vals[k]:
                        flag = True
                        break
                
                if not flag:
                    longest = max(longest, j - i + 1)

        return longest
                    
