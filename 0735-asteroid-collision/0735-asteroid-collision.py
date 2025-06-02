class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        final_state = [asteroids[0]]
        for a in asteroids[1:]:
            if len(final_state) == 0:
                final_state.append(a)
                continue

            prev = final_state[-1]
            # Prev going right and current going left, will hit
            while prev > 0 and a < 0 and abs(a) > abs(prev):
                final_state.pop()
                if len(final_state) > 0:
                    prev = final_state[-1]
                else:
                    break
            
            if len(final_state) == 0:
                final_state.append(a)
                continue
            
            # Edge case where asteroids cancel out each other
            if a < 0 and a == -1 * prev:
                final_state.pop()

            # Same sign or prev and cur asteroids not moving towards each other
            if not (a < 0 and prev > 0):
                final_state.append(a)

        return final_state


                

