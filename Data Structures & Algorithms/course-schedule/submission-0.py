class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 时间	O(V + E)	V = 课程数，E = 先修关系数，每个节点和边各访问一次
        # 空间	O(V + E)	邻接表 O(V+E) + state 数组 O(V) + 递归栈 O(V)

        # 建邻接表：graph[i] 存课程 i 的所有先修课
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0=未访问, 1=正在查（这条路上）, 2=查完了（安全）
        state = [0] * numCourses

        def has_cycle(course):
            # 正在查的过程中又遇到了 → 有环
            if state[course] == 1:
                return True
            # 之前查完了，确认安全，跳过
            if state[course] == 2:
                return False

            # 标记"我正在查这门课"
            state[course] = 1

            # 去查每个先修课
            for prereq in graph[course]:
                # 某个先修课有环 → 我也有环
                if has_cycle(prereq):
                    return True

            # 所有依赖都没问题，标记"查完了"
            state[course] = 2
            return False

        # 每门课都检查一遍（图可能不是全部连在一起的）
        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True