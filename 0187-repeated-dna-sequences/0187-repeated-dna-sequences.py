class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = s[:10]
        seen = set([seq])
        ans = set()
        for c in s[10:]:
            seq = seq[1:] + c
            if seq in seen:
                ans.add(seq)
            else:
                seen.add(seq)

        return list(ans)
