class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # IDEA:
        # each course is a node, and each directed edge is a prereq
        # we want an order of courses such that all prereqs of a course are taken before taking it

        # USING DFS:
        # Detect Cycles (0 -> 1 -> 2 -> 0)

        # a course has 3 states:
        # visited -> crs has been added to the output
        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle
        output = []
        visited = set() # tracks fully processed courses
        cycle = set() # tracks the current DFS path (for cycle detection)

        def dfs(crs):
            """
            For each course (crs), we want to run DFS through all prereqs of this crs.
            After processing the prereqs, we can finally add the course to the result
            """
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
            
        return output


