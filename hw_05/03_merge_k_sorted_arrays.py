import heapq


def solution(arrays: list[list[int]]) -> list[int]:
    res = []
    heap = []  
    for i in range(len(arrays)):
        arr = arrays[i]
        if len(arr)>0:
            heapq.heappush(heap, (arr[0], i, 0))

    while len(heap) > 0:
        val, arr_idx, val_idx = heapq.heappop(heap)
        res.append(val)

        if val_idx + 1 < len(arrays[arr_idx]):
            elem = arrays[arr_idx][val_idx + 1]
            heapq.heappush(heap, (elem, arr_idx, val_idx + 1))
    return res




def test():
    test_data = [
        {"arrays": [], "answer": []},
        {"arrays": [[]], "answer": []},
        {"arrays": [[], [], []], "answer": []},
        {"arrays": [[1]], "answer": [1]},
        {"arrays": [[1, 2, 3]], "answer": [1, 2, 3]},
        {"arrays": [[], [1, 3], []], "answer": [1, 3]},
        {"arrays": [[1, 3, 5], [2, 4, 6]], "answer": [1, 2, 3, 4, 5, 6]},
        {"arrays": [[1, 4], [2, 5], [3, 6]], "answer": [1, 2, 3, 4, 5, 6]},
        {"arrays": [[3], [1], [2]], "answer": [1, 2, 3]},
        {"arrays": [[1, 2], [3, 4]], "answer": [1, 2, 3, 4]},
        {"arrays": [[3, 4], [1, 2]], "answer": [1, 2, 3, 4]},
        {"arrays": [[1, 1], [1], [1, 1]], "answer": [1, 1, 1, 1, 1]},
        {"arrays": [[0, 0], [], [0]], "answer": [0, 0, 0]},
        {"arrays": [[-5, -1], [-4, -2]], "answer": [-5, -4, -2, -1]},
        {"arrays": [[-3, 0, 4], [-2, 0, 5]], "answer": [-3, -2, 0, 0, 4, 5]},
        {"arrays": [[1, 2, 3, 4, 5], [0], [6, 7]], "answer": [0, 1, 2, 3, 4, 5, 6, 7]},
        {"arrays": [[], [2, 8], [], [1, 3, 9], []], "answer": [1, 2, 3, 8, 9]},
    ]
    for test_info in test_data:
        arrays = [nums.copy() for nums in test_info["arrays"]]
        result = solution(arrays)
        err_str = (
            f"\nTest failed for input: arrays={test_info['arrays']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Кидаю в мин-кучу первый элемент каждого непустого массива.
    Достаю минимум, добавляю в ответ и кидаю в кучу следующий элемент
    из того же массива. Повторяю, пока куча не пустая
    В куче максимум K элементов, всего достаю N элементов.
    По времени O(K + N * log(K + 1)), по памяти O(K) на кучу
    и O(N) на ответ.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
