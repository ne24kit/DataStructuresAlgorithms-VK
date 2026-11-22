from math import inf

def solution(coins: list[int], amount: int) -> int:
    dp = [inf] * (amount + 1)
    dp[0] = 0
    for amount_i in range(1, amount + 1):
        for c in coins:
            if c <= amount_i:
                dp[amount_i] = min(dp[amount_i], dp[amount_i - c] + 1)
    
    return -1 if dp[amount] == inf else dp[amount]

def test():
    test_data = [
        {"coins": [1, 2, 5], "amount": 11, "answer": 3},
        {"coins": [2], "amount": 3, "answer": -1},
        {"coins": [1], "amount": 0, "answer": 0},
        {"coins": [7], "amount": 7, "answer": 1},
        {"coins": [2], "amount": 6, "answer": 3},
        {"coins": [5, 2], "amount": 6, "answer": 3},
        {"coins": [4, 1, 3], "amount": 6, "answer": 2},
        {"coins": [], "amount": 4, "answer": -1},
        {"coins": [], "amount": 0, "answer": 0},
    ]
    for test_info in test_data:
        coins = test_info["coins"].copy()
        amount = test_info["amount"]
        result = solution(coins, amount)
        err_str = (
            f"\nTest failed for input: coins={test_info['coins']}, amount={amount}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    В dp[s] храню минимум монет для суммы s. Начинаю с dp[0] = 0, остальные значения равны inf.
    Если последняя монета имеет номинал c, до неё нужно собрать s - c.
    Беру минимум dp[s - c] + 1 по всем c <= s. Если dp[amount] осталось inf, возвращаю -1.
    Время O(amount * len(coins)), память O(amount).
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
