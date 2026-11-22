def solution(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        profit = max(profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return profit


def test():
    test_data = [
        {"prices": [], "answer": 0},
        {"prices": [5], "answer": 0},
        {"prices": [8, 9, 3, 7, 4, 16, 12], "answer": 13},
        {"prices": [1, 2, 3, 4, 5, 6, 7], "answer": 6},
        {"prices": [8, 7, 6, 5, 4, 3, 2], "answer": 0},
        {"prices": [4, 4, 4], "answer": 0},
        {"prices": [10, 2, 8, 1], "answer": 6},
        {"prices": [1, 3, 2, 4], "answer": 3},
    ]
    for test_info in test_data:
        prices = test_info["prices"].copy()
        result = solution(prices)
        err_str = (
            f"\nTest failed for input: prices={test_info['prices']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Храню min_price среди предыдущих дней и profit максимальный.
    Один проход даёт O(n) времени и O(1) дополнительной памяти.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
