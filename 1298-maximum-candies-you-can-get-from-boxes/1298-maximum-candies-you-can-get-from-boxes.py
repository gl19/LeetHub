class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        total_candies = 0
        keys_had = set()
        boxes_had = initialBoxes
        boxes_visited = set()

        while True:
            should_continue = False
            for i in boxes_had:                
                if i not in boxes_visited and (status[i] == 1 or i in keys_had):
                    total_candies += candies[i]
                    keys_had.update(keys[i])
                    boxes_had.extend(containedBoxes[i])
                    boxes_visited.add(i)
                    should_continue = True
            
            if not should_continue:
                break

        return total_candies

