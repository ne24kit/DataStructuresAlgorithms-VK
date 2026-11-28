from heapq import heappop, heappush
from math import inf


def solution(graph: dict[int, list[tuple[int, int]]], start: int) -> dict[int, float]:
    distances = {node: inf for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        distance, node = heappop(heap)
        if distance != distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(heap, (new_distance, neighbor))

    return distances


def test():
    test_data = [
        {"graph": {5: []}, "start": 5, "answer": {5: 0}},
        {
            "graph": {1: [(2, 10), (3, 2)], 2: [(4, 1)], 3: [(2, 3)], 4: []},
            "start": 1,
            "answer": {1: 0, 2: 5, 3: 2, 4: 6},
        },
        {
            "graph": {1: [], 2: [(3, 0)], 3: [(2, 0), (4, 2)], 4: []},
            "start": 2,
            "answer": {1: inf, 2: 0, 3: 0, 4: 2},
        },
        {
            "graph": {1: [(2, 1)], 2: [], 3: [(2, 4)]},
            "start": 2,
            "answer": {1: inf, 2: 0, 3: inf},
        },
    ]
    for test_info in test_data:
        graph = test_info["graph"]
        start = test_info["start"]
        result = solution(graph, start)
        err_str = (
            f"\nTest failed for input: graph={graph}, start={start}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Из кучи беру вершину с наименьшим расстоянием. Устаревшие записи пропускаю.
    Если через неё путь до соседа короче, обновляю расстояние и кладу новую пару в кучу.
    Каждое ребро проверяю максимум раз. Для простого графа операция с кучей стоит O(log V),
    поэтому общее время O((V + E) log V).
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
