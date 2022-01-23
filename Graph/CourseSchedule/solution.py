# PROBLEM STATEMENT
# https://leetcode.com/problems/course-schedule/
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.canFinishAdjList(numCourses, prerequisites)

    # Time Complexity: O(V + E) where V and E are the number courses and prerequisites
    # Space Complexity: O(V + E) where V and E are the number courses and prerequisites
    def canFinishAdjList(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(adjList: List[List[int]], isVisited: List[bool], canFinish: List[bool], index: int) -> bool:
            if isVisited[index]:
                return False
            elif canFinish[index]:
                return True
            else:
                isVisited[index] = True

                for prereq in adjList[index]:
                    if not dfs(adjList, isVisited, canFinish, prereq):
                        return False

                canFinish[index] = True
                isVisited[index] = False

                return True

        adjList = [[] for _ in range(numCourses)]
        isVisited = [False for _ in range(numCourses)]
        canFinish = [False for _ in range(numCourses)]

        for p in prerequisites:
            adjList[p[0]].append(p[1])

        for i in range(len(adjList)):
            if not dfs(adjList, isVisited, canFinish, i):
                return False

        return True