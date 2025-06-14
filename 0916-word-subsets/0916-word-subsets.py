class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        master_d = defaultdict(int)
        for word in words2:
            d_word = Counter(word)
            for letter in d_word.keys():
                master_d[letter] = max(master_d[letter], d_word[letter])

        ret = []
        for word in words1:
            d_word = Counter(word)
            flag = False
            for char in master_d.keys():
                if char not in d_word or master_d[char] > d_word[char]:
                    flag = True
                    break

            if not flag:
                ret.append(word)

        return ret

            

        
        