def solution(x: int) -> int:
    if x < 2:
        return x
    l = 2
    r = x // 2 
    while l <= r:
        mid = (l + r) // 2 
        mid_2 = mid * mid
        if mid_2 == x:
            return mid 
        elif mid_2 < x:
            l = mid + 1
        else:
            r = mid - 1
    return r


def test():

    test_data = [
        {"x": 0, "answer": 0},
        {"x": 1, "answer": 1},
        {"x": 2, "answer": 1},
        {"x": 3, "answer": 1},
        {"x": 4, "answer": 2},
        {"x": 8, "answer": 2},
        {"x": 9, "answer": 3},
        {"x": 10, "answer": 3},
        {"x": 15, "answer": 3},
        {"x": 16, "answer": 4},
        {"x": 17, "answer": 4},
        {"x": 99, "answer": 9},
        {"x": 100, "answer": 10},
        {"x": 101, "answer": 10},
        {"x": 10**18 - 1, "answer": 10**9 - 1},
        {"x": 10**18, "answer": 10**9},
        {"x": 10**18 + 1, "answer": 10**9},
    ]
    for test_info in test_data:
        result = solution(test_info["x"])
        err_str = (
            f"\nTest failed for input: x={test_info['x']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Для x < 2 возвращаем x. При x >= 4 корень лежит между 2 и x // 2.
    Для 2 и 3 диапазон пуст, поэтому возвращается r = 1.
    На каждом шаге делим диапазон пополам -> O(log x).
    Если точный корень не найден, r содержит целую часть корня.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
