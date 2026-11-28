def solution(graph: dict[int, list[int]]) -> bool:
    if len(graph) == 0:
        return False
    
    start = next(iter(graph))

    queue = [start]
    visited = set()
    parent = {start: None}
    while queue:
        node = queue[0]
        queue = queue[1:]
        visited.add(node)
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
                parent[n] = node
            elif parent[node] != n:
                return False
        
    return len(visited) == len(graph)


def test():
    test_data = [
        {"graph": {}, "answer": False},
        {"graph": {1: []}, "answer": True},
        {"graph": {1: [2], 2: [1]}, "answer": True},
        {"graph": {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}, "answer": True},
        {"graph": {1: [2], 2: [1], 3: []}, "answer": False},
        {"graph": {1: [2, 3], 2: [1, 3], 3: [1, 2]}, "answer": False},
        {"graph": {1: [], 2: [3, 4], 3: [2, 4], 4: [2, 3]}, "answer": False},
        {"graph": {1: [1]}, "answer": False},
    ]
    for test_info in test_data:
        graph = test_info["graph"]
        result = solution(graph)
        err_str = (
            f"\nTest failed for input: graph={graph}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result is test_info["answer"], err_str


def answer_on_question():
    ans = """
    Запускаю BFS из одной вершины. Если встречаю посещённого соседа, кроме родителя, значит, есть цикл.
    Если обошёл все вершины, граф связен. Связный неориентированный граф без циклов — дерево по определению.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
