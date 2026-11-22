def solution(n: int) -> list[list[int]]:
    if n == 0:
        return []
    dp = [[1]]
    for r in range(1, n):
        row = [1]
        for c in range(1, r):
            row.append(dp[r-1][c] + dp[r-1][c-1])
        row.append(1)
        dp.append(row)

    return dp
    
    


def test():
    test_data = [
        {"n": 0, "answer": []},
        {"n": 1, "answer": [[1]]},
        {"n": 2, "answer": [[1], [1, 1]]},
        {"n": 3, "answer": [[1], [1, 1], [1, 2, 1]]},
        {"n": 5, "answer": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]},
    ]
    for test_info in test_data:
        n = test_info["n"]
        result = solution(n)
        err_str = (
            f"\nTest failed for input: n={n}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Начинаю с [1]. По краям каждой новой строки ставлю 1, а внутри складываю
    два соседних числа из предыдущей строки.
    Время и память O(n^2), потому что строю и храню n(n + 1) / 2 чисел.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
