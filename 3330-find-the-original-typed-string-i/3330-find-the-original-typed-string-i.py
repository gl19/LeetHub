class Solution:
    def possibleStringCount(self, word: str) -> int:
        possibilities = 1
        run_len = 0
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                run_len += 1
            else:
                if run_len > 0:
                    possibilities += run_len

                run_len = 0

        if run_len != 0:
            possibilities += run_len

        return possibilities