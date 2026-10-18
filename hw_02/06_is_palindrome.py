

def solution(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while right > left:
        if s[left] != s[right]:
            return False
        right -= 1
        left  += 1 

    return True


def test():
    test_data = [
        {
            "s": "",
            "answer": True
        },
        {
            "s": "a",
            "answer": True
        },
        {
            "s": "aa",
            "answer": True
        },
        {
            "s": "ab",
            "answer": False
        },
        {
            "s": "топот",
            "answer": True
        },
        {
            "s": "abba",
            "answer": True
        },
        {
            "s": "abca",
            "answer": False
        },
        {
            "s": "python",
            "answer": False
        },
        {
            "s": "aaaa",
            "answer": True
        },
        {
            "s": "1221",
            "answer": True
        },
        {
            "s": "Топот",
            "answer": False
        },
        {
            "s": "а б а",
            "answer": True
        },
        {
            "s": "аба ",
            "answer": False
        },
        {
            "s": "абоба",
            "answer": True
        },
        {
            "s": "хахах",
            "answer": True
        },
        {
            "s": "наган",
            "answer": True
        },
    ]
    for test_info in test_data:
        result = solution(test_info["s"])
        err_str = (
            f"\nTest failed for input: s={test_info['s']!r}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Сравниваем символы с двух концов, двигая указатели к середине.
    При несовпадении возвращаем False, иначе после обхода - True.
    Не более n // 2 сравнений -> время - O(n); память - O(1) (два указателя и всё).
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
