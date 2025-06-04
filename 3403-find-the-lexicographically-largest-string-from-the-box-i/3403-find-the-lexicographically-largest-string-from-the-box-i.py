class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        def larger_lex(a, b):
            for c1, c2 in zip(a, b):
                if ord(c1) > ord(c2):
                    return a
                elif ord(c1) < ord(c2):
                    return b

            if len(a) > len(b):
                return a
            else:
                return b

        if numFriends == 1:
            return word

        max_word = ''
        for i, c in enumerate(word):
            if numFriends - 1 > i:
                candidate = word[i:len(word) + i - numFriends + 1]
            else:
                candidate = word[i:]

            if larger_lex(candidate, max_word) == candidate:
                max_word = candidate              

        return max_word

        
        

