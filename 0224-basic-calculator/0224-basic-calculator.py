class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        
        # Base case
        plus_count = s.count('+')
        minus_count = s.count('-')
        paren_count = s.count('(') + s.count(')')
        if paren_count + plus_count + minus_count == 0 or paren_count == 0 and plus_count == 0 and minus_count == 1 and s[0] == '-':
            return int(s)

        numbers = 0
        left_bracket = None
        num_open_brackets = 0
        cur_num = ''
        is_cur_num_neg = False
        for i, c in enumerate(s):
            if left_bracket is not None:
                if c == ')':
                    if num_open_brackets == 1:
                        calc_number = self.calculate(s[left_bracket + 1:i])
                        cur_num = str(calc_number)
                        left_bracket = None

                    num_open_brackets -=1
                elif c == '(':
                    num_open_brackets += 1

                continue

            if c == '(':
                left_bracket = i
                num_open_brackets = 1
            elif c == '+':
                numbers += -1 * int(cur_num) if is_cur_num_neg else int(cur_num)
                cur_num = ''
                is_cur_num_neg = False
            elif c == '-':
                if cur_num != '':
                    numbers += -1 * int(cur_num) if is_cur_num_neg else int(cur_num)
                    cur_num = ''

                is_cur_num_neg = True
            else:
                cur_num += c

        if cur_num != '':
            numbers += -1 * int(cur_num) if is_cur_num_neg else int(cur_num)

        return numbers

