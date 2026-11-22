def solution(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    best_start = 0
    best_len = 0

    for length in range(1, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            dp[l][r] = s[l] == s[r] and (length <= 2 or dp[l + 1][r - 1])

            if dp[l][r] and length > best_len:
                best_start = l
                best_len = length

    return s[best_start:best_start + best_len]


def test():
    test_data = [
        {"s": "", "answers": [""]},
        {"s": "a", "answers": ["a"]},
        {"s": "abc", "answers": ["a", "b", "c"]},
        {"s": "babad", "answers": ["bab", "aba"]},
        {"s": "cbbd", "answers": ["bb"]},
        {"s": "racecar", "answers": ["racecar"]},
        {"s": "aaaa", "answers": ["aaaa"]},
        {"s": "xabccbay", "answers": ["abccba"]},
    ]
    for test_info in test_data:
        s = test_info["s"]
        result = solution(s)
        err_str = (
            f"\nTest failed for input: s={s!r}\n"
            f"Expected one of: {test_info['answers']}, but got: {result!r}"
        )
        assert result in test_info["answers"], err_str


def answer_on_question():
    ans = """
    В dp[l][r] отмечаю, является ли подстрока палиндромом. Иду от коротких к длинным.
    Края должны совпадать, а при длине больше 2 середина должна быть палиндромом.
    Запоминаю начало и длину лучшего палиндрома. Время и память O(n^2) (ну и ладно)
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
