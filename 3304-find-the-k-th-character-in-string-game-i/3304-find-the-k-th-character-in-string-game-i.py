class Solution:
    def kthCharacter(self, k: int) -> str:
        print(ord('z'))
        cur = 'a'
        while len(cur) < k:
            suffix = ''
            for c in cur:
                if c == 'z':
                    suffix += 'a'
                else:
                    suffix += chr(ord(c) + 1)

            cur += suffix

        return cur[k - 1]