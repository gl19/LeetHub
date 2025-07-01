class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        if limit <= 5:
            return []

        # try single digit last:
        def helper(magnitude):
            ret = []
            message_num = 1
            cur_msg = ''
            for c in message:
                suffix = f"<{message_num}/"
                if len(suffix) + magnitude + 1 >= limit:
                    return []
                
                cur_msg += c
                if len(suffix) + len(cur_msg) + magnitude + 1 == limit:
                    ret.append(f"{cur_msg}{suffix}")
                    message_num += 1
                    cur_msg = ''
                    
            if cur_msg == '':
                message_num -= 1
            else:
                suffix = f"<{message_num}/"
                ret.append(f"{cur_msg}{suffix}")

            if floor(math.log(message_num, 10)) + 1 > magnitude:
                return helper(magnitude + 1)

            total_msg = len(ret)
            for i in range(total_msg):
                ret[i] += f"{total_msg}>"

            return ret

        return helper(1)


        