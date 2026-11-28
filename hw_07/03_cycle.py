def dfs(graph, node, visited, parent):
    visited.add(node)
    for n in graph[node]:
        if parent != n:
            if n in visited or dfs(graph, n, visited, node):
                return True

    return False


def solution(graph: dict[int, list[int]]) -> bool:
    visited = set()
    flag = False
    for node in graph:
        parent = None
        if node not in visited:
            flag = dfs(graph, node, visited, parent)
            if flag:
                return flag
            
    return flag


def test():
    test_data = [
        {"graph": {}, "answer": False},
        {"graph": {1: []}, "answer": False},
        {"graph": {1: [2], 2: [1]}, "answer": False},
        {"graph": {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}, "answer": False},
        {"graph": {1: [2, 3], 2: [1, 3], 3: [1, 2]}, "answer": True},
        {"graph": {1: [], 2: [3, 4], 3: [2, 4], 4: [2, 3]}, "answer": True},
        {"graph": {1: [], 2: [3], 3: [2]}, "answer": False},
        {"graph": {1: [1]}, "answer": True},
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
    Обхожу каждую компоненту через DFS. Ребро к родителю пропускаю, потому что по нему я пришёл.
    Если другой сосед уже в visited, нашёл цикл. Время O(V + E), память O(V) на visited и стек рекурсии.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
