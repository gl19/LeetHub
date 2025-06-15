class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        max_replace = defaultdict(str)
        min_replace = defaultdict(str)
        max_num = ''
        min_num = ''
        for i, digit in enumerate(num_str):
            if digit in max_replace:
                max_num += max_replace[digit]
            elif len(max_replace.keys()) == 0:
                if digit != '9':
                    max_replace[digit] = '9'
                
                max_num += '9'
            else:
                max_num += digit
            
            if digit in min_replace:
                min_num += min_replace[digit]
            elif len(min_replace.keys()) == 0:
                if i == 0:
                    if digit != '1':
                        min_replace[digit] = '1'

                    min_num += '1'
                elif digit == '0' or digit == num_str[0]:
                    min_num += digit
                else:
                    min_replace[digit] = '0'
                    min_num += '0'
            else:
                min_num += digit

        return int(max_num) - int(min_num)
