def dfs(graph, node, visited, component):
    visited.add(node)
    component.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, component)

def solution(graph: dict[int, list[int]]) -> list[list[int]]:
    visited = set()
    all_components = []
    for node in graph:
        if node not in visited:
            component = []
            dfs(graph, node, visited, component)
            all_components.append(component)
    return all_components


def test():
    test_data = [
        {"graph": {}, "answer": []},
        {"graph": {1: []}, "answer": [[1]]},
        {"graph": {1: [], 2: [], 3: []}, "answer": [[1], [2], [3]]},
        {"graph": {10: [20], 20: [10, 30], 30: [20]}, "answer": [[10, 20, 30]]},
        {"graph": {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: []}, "answer": [[1, 2, 3], [4]]},
        {"graph": {1: [2], 2: [1], 3: [4], 4: [3], 5: []}, "answer": [[1, 2], [3, 4], [5]]},
    ]
    for test_info in test_data:
        graph = test_info["graph"]
        result = solution(graph)
        err_str = (
            f"\nTest failed for input: graph={graph}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert isinstance(result, list) and all(isinstance(part, list) for part in result), err_str
        assert sorted(sorted(part) for part in result) == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Из каждой непосещённой вершины запускаю DFS и собираю все достижимые вершины в один список.
    Время O(V + E), память O(V) на visited, рекурсию и ответ.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
