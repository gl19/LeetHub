class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Even though it is round based, I don't think it should take more than 2 rounds
        # Case 1: Unequal R to D: senators cancel out and can win in first round
        # Case 2: Equal R to D: first senator wins (Example 1)
        banned_r = 0
        banned_d = 0
        x = 2
        while len(senate) > 0:
            next_senate = []
            for senator in senate:
                if senator == 'R':
                    if banned_r > 0:
                        banned_r -= 1
                    else:
                        banned_d += 1
                        next_senate.append('R')
                elif senator == 'D':
                    if banned_d > 0:
                        banned_d -= 1
                    else:
                        banned_r += 1
                        next_senate.append('D')
            
            new_senate_fixed = []
            for senator in next_senate:
                if senator == 'R' and banned_r > 0:
                    banned_r -= 1
                elif senator == 'D' and banned_d > 0:
                    banned_d -= 1
                else:
                    new_senate_fixed.append(senator)
                    
            if banned_r > 0:
                return 'Dire'

            if banned_d > 0:
                return 'Radiant'

            senate = new_senate_fixed

            # print(senate)

        if banned_r > 0:
            return 'Dire'

        return 'Radiant'

        