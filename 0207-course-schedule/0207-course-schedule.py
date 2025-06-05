class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[a].add(b)
            if b not in graph:
                graph[b]

        cycle = False
        def dfs(cur, visited):
            nonlocal cycle
            if cur in visited:
                cycle = True
                return

            visited.add(cur)
            for neighbor in graph[cur]:
                dfs(neighbor, visited.copy())
        
        for course in graph.keys():
            if cycle:
                return False
            
            dfs(course, set())

        if cycle:
            return False

        return len(graph.keys()) <= numCourses