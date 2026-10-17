def solution(a: str, b: str):
    p_a = 0
    p_b = 0
    len_a = len(a)
    len_b = len(b)
    while p_a < len_a and p_b < len_b:
        if a[p_a] == b[p_b]:
            p_a += 1
        p_b += 1
    return p_a == len_a


def test():
    test_data = [
        {
            "a": "abc",
            "b": "ahbgdc",
            "answer": True
        },
        {
            "a": "axc",
            "b": "ahbgdc",
            "answer": False
        },
        {
            "a": "abc",
            "b": "abc",
            "answer": True
        },
        {
            "a": "",
            "b": "abc",
            "answer": True
        },
        {
            "a": "",
            "b": "",
            "answer": True
        },
        {
            "a": "abc",
            "b": "",
            "answer": False
        },
        {
            "a": "abcd",
            "b": "abc",
            "answer": False
        },
        {
            "a": "abc",
            "b": "acb",
            "answer": False
        },
        {
            "a": "aaa",
            "b": "abaca",
            "answer": True
        },
        {
            "a": "aaa",
            "b": "aa",
            "answer": False
        },
        {
            "a": "cat",
            "b": "xxcatyy",
            "answer": True
        },
    ]
    for test_info in test_data:
        result = solution(test_info["a"], test_info["b"])
        err_str = (
            f"\nTest failed for input: "
            f"a={test_info['a']!r}, b={test_info['b']!r}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Идём по строке b и ищем символы строки a в исходном порядке.
    При совпадении передвигаем указатель в a, указатель в b двигаем всегда.
    Несовпадающие символы в b считаем добавленными.
    Если нашли все символы a, строку b можно получить добавлением символов к a.
    Иначе возвращаем False. Пустая строка a подходит для любой строки b.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
