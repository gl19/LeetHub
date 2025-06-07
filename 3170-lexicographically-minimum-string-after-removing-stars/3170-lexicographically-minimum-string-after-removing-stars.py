class Solution:
    def clearStars(self, s: str) -> str:
        locs = [[] for _ in range(26)]
        ret = []
        for i, c in enumerate(s):
            if c == '*':
                for loc in locs:
                    if len(loc) > 0:
                        ret[loc.pop()] = ""
                        break

                ret.append("")
            else:
                ret.append(c)
                locs[ord(c) - ord('a')].append(i)

        print(ret)
        return ''.join(ret)
        