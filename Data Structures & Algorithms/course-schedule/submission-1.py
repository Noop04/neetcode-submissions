class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}
        for i in range(numCourses):
            pre[i] = []
        for a,b in prerequisites:
            pre[a].append(b)
        
        seen = set()

        def dfs(course):
            if course in seen:
                return False
            if pre[course] == []:
                return True
            
            seen.add(course)
            for prereq in pre[course]:
                if not dfs(prereq):
                    return False
            seen.remove(course)
            return True

                
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            

