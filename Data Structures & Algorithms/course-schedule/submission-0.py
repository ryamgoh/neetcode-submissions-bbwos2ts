class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create our preMap

        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # now we built the preMap,
        # we can traverse it!

        # but we should also store all courses in case we visit again.
        currently_visiting = set()

        def dfs(crs) -> bool:

            if crs in currently_visiting:
                # we found a cycle
                return False
            if preMap[crs] == []:
                return True

            currently_visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            currently_visiting.remove(crs)
            preMap[crs] = []

            return True



        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
