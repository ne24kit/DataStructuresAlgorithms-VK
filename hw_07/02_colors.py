def dfs(graph, node, visited, color):
    visited[node] = color
    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited, color)


def solution(graph: dict[int, list[int]]) -> dict[int, int]:
    visited = {}
    color = 0
    for node in graph:
        if node not in visited:
            color += 1
            dfs(graph, node, visited, color)
    return visited


def test():
    test_data = [
        {"graph": {}, "answer": []},
        {"graph": {7: []}, "answer": [[7]]},
        {"graph": {3: [], 1: [], 2: []}, "answer": [[3], [1], [2]]},
        {"graph": {10: [20], 20: [10, 30], 30: [20]}, "answer": [[10, 20, 30]]},
        {"graph": {1: [3, 5], 2: [4], 3: [1, 5], 4: [2], 5: [1, 3], 6: []},
         "answer": [[1, 3, 5], [2, 4], [6]]},
    ]
    for test_info in test_data:
        graph = test_info["graph"]
        components = test_info["answer"]
        result = solution(graph)
        err_str = f"Test failed for graph={graph}, components={components}, got {result}"
        assert isinstance(result, dict) and result.keys() == graph.keys(), err_str
        assert all(type(color) is int for color in result.values()), err_str
        assert set(result.values()) == set(range(1, len(components) + 1)), err_str
        for component in components:
            assert len({result[node] for node in component}) == 1, err_str


def answer_on_question():
    ans = """
    Когда встречаю неокрашенную вершину, беру следующий цвет и запускаю DFS.
    Всем вершинам этой компоненты записываю один цвет в visited.
    Время O(V + E), память O(V) на словарь и стек рекурсии.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
