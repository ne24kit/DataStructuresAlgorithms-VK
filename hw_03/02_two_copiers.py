def solution(n: int, x: int, y: int) -> int:
    
    l = 0
    r = (n - 1) * max(x, y)

    while l + 1 < r:
        mid = (l + r) // 2
        if mid // x + mid // y < n - 1:
            l = mid
        else:
            r = mid
        

    return r + min(x, y)


def test():

    test_data = [
        {"n": 1, "x": 2, "y": 3, "answer": 2},
        {"n": 1, "x": 5, "y": 2, "answer": 2},
        {"n": 2, "x": 2, "y": 3, "answer": 4},
        {"n": 3, "x": 2, "y": 3, "answer": 5},
        {"n": 4, "x": 1, "y": 1, "answer": 3},
        {"n": 5, "x": 1, "y": 2, "answer": 4},
        {"n": 5, "x": 2, "y": 1, "answer": 4},
        {"n": 5, "x": 3, "y": 3, "answer": 9},
        {"n": 6, "x": 2, "y": 3, "answer": 8},
        {"n": 10, "x": 1, "y": 100, "answer": 10},
        {"n": 10**9, "x": 1, "y": 1, "answer": 500000001},
    ]
    for test_info in test_data:
        result = solution(test_info["n"], test_info["x"], test_info["y"])
        err_str = (
            f"\nTest failed for input: "
            f"n={test_info['n']}, x={test_info['x']}, y={test_info['y']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Первую копию делаем за min(x, y), затем работают оба ксерокса.
    За t минут они сделают t // x + t // y новых копий.
    Если это количество >= n - 1, времени достаточно и пробуем меньшее,
    иначе увеличиваем время.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
