def solution(n: int) -> int:
    dp = [1, 2] # так называемая база
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])

    return dp[n]


def test():
    test_data = [
        {"n": 0, "answer": 1}, # []
        {"n": 1, "answer": 2}, # [0], [1]
        {"n": 2, "answer": 3}, # [00],[01],[10] 
        {"n": 3, "answer": 5},
        {"n": 4, "answer": 8},
        {"n": 5, "answer": 13},
        {"n": 10, "answer": 144},
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
    В dp[i] храню кол-во послед. длины i без двух единиц подряд.
    При i = 0 есть одна пустая послед., поэтому dp[0] = 1.
    При i = 1 подходят 0 и 1, поэтому dp[1] = 2.
    При i = 2 подходят 00, 01 и 10, поэтому dp[2] = 3.

    Для i >= 2 смотрю на последний символ.
    Если это 0, его можно приписать к любой послед.
    длины i - 1, таких вариантов dp[i - 1].
    Если это 1, то перед ней обязательно стоит 0!!!. Значит приписываем мы 01
    к любой послед. уже длины i - 2, таких вариантов dp[i - 2].
    
    Делаю O(n) сложений и храню O(n) чисел в массиве dp.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
