class Solution:
    def robotWithString(self, s: str) -> str:
        def helper(left, idx, ret):
            if idx == len(s):
                left.reverse()
                return ret + left
            
            while len(left) > 0 and left[-1] <= smallest_val_right[idx]:
                ret.append(left.pop())

            while idx < len(s):
                if s[idx] != smallest_val_right[idx]:
                    left.append(s[idx])
                else:
                    ret.append(s[idx])
                    break

                idx += 1

            return helper(left, idx + 1, ret)

        # Set up right
        smallest_val_right = [None for _ in s]
        smallest_val = chr(1000)
        for i in range(len(s) - 1, -1, -1):
            if s[i] < smallest_val:
                smallest_val = s[i]

            smallest_val_right[i] = smallest_val



        return ''.join(helper([], 0, []))

            

            
        

        





        321235312312

        
        


        