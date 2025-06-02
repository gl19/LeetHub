class Solution:
    def predictPartyVictory(self, senate: str) -> str:
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

        if banned_r > 0:
            return 'Dire'

        return 'Radiant'

        