class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        dictionary = {}
        seen_words = set()
        for c, word in zip(pattern, words):
            if c in dictionary:
                if dictionary[c] != word:
                    return False

            else:
                if word in seen_words:
                    return False

                dictionary[c] = word
                seen_words.add(word)


        return True