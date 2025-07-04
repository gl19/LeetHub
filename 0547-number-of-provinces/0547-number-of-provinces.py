class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
                
            count += 1
            to_visit = [i]
            while to_visit:
                city = to_visit.pop()
                if city in visited:
                    continue

                visited.add(city)
                for j, is_neighbor in enumerate(isConnected[city]):
                    if i != j and is_neighbor == 1 and j not in visited:
                        to_visit.append(j)

        return count
