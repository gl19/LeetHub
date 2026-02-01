class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        
        # down up start: 1 -> 3, even idx are up
        dp_du = [0 for _ in range(n - 1)]
        # up down start: 3 -> 1, odd idx are up
        dp_ud = [0 for _ in range(n - 1)]

        is_du_up = True
        is_ud_up = False
        for i in range(1, n):
            is_up = nums[i - 1] < nums[i]
            is_down = nums[i - 1] > nums[i]

            dp_du[i - 1] = (is_du_up and is_up) or (not is_du_up and is_down)
            dp_ud[i - 1] = (is_ud_up and is_up) or (not is_ud_up and is_down)

            # swap up-down and down-up, vice versa
            is_du_up, is_ud_up = is_ud_up, is_du_up

        # adds the zigzag seq length backwards for earier compute later
        for i in range(n - 3, -1, -1):
            if dp_du[i] == 1 and dp_du[i + 1] > 0:
                dp_du[i] += dp_du[i + 1]
            
            if dp_ud[i] == 1 and dp_ud[i + 1] > 0:
                dp_ud[i] += dp_ud[i + 1]


        # print("down-up:", dp_du)
        # print("up-down:", dp_ud)

        max_seq = max(max(dp_du), max(dp_ud))
        # cur_seq just keeps track of the length of the seq before switching
        cur_seq_du = 0
        cur_seq_ud = 0
        for i in range(n - 2):
            # du start switch to ud
            if dp_du[i] == 0:
                if dp_ud[i + 1] > 0:
                    max_seq = max(max_seq, cur_seq_du + dp_ud[i + 1])

                cur_seq_du = 0
            elif cur_seq_du == 0:
                # reset seq count when seq breaks
                cur_seq_du = dp_du[i]

            # ud start switch to du
            if dp_ud[i] == 0:
                if dp_du[i + 1] > 0:
                    max_seq = max(max_seq, cur_seq_ud + dp_du[i + 1])

                cur_seq_ud = 0
            elif cur_seq_ud == 0:
                # reset seq count when seq breaks
                cur_seq_ud = dp_ud[i]

        return max_seq + 1


