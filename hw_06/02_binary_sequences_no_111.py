def solution(n: int) -> int:
    dp = [1, 2, 4] # так называемая база
    for i in range(3, n + 1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])

    return dp[n]




def test():
    test_data = [
        {"n": 0, "answer": 1},
        {"n": 1, "answer": 2},
        {"n": 2, "answer": 4},
        {"n": 3, "answer": 7},
        {"n": 4, "answer": 13},
        {"n": 5, "answer": 24},
        {"n": 10, "answer": 504},
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
    как в прошлой задаче только сейчас:
    ***0 за dp[i-1]
    **01 за dp[i-2]
    *011 за dp[i-3]
    база:
    n=0: []
    n=1: [0],[1]
    n=2: [00],[10],[01],[11]
    O(n) время, память 
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
