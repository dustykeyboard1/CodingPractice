"""
Implements the topological sort DFS to solve the course schedule problem
"""


def dfs(graph, vertex, path, order, visited):
    path.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph, neighbor, path, order, visited):
                return False
    path.remove(vertex)
    order.append(vertex)
    return True


def course_schedule(n, prereqs):
    graph = [[] for i in range(n)]
    for pre in prereqs:
        graph[pre[1]].append(pre[0])
    visited = set()
    path = set()
    order = []
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path, order, visited):
                return False

    return True


def main():
    n = 6
    pre = [[3, 0], [0, 1], [1, 3], [2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]  ## False
    print(course_schedule(n, pre))
    pre = [[3, 0], [1, 3], [2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]  ## True
    print(course_schedule(n, pre))


if __name__ == "__main__":
    main()
