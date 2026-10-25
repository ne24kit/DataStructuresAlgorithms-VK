def solution(a: str, b: str) -> str:
    hash_table = {}
    for s_b in b:
        hash_table[s_b] = hash_table.get(s_b, 0) + 1

    for s_a in a:
        if s_a in hash_table:
            hash_table[s_a] -= 1
            if hash_table[s_a] == 0:
                hash_table.pop(s_a)

    for s, cnt in hash_table.items():
        if cnt == 1:
            return s

    return ""


def test():
    # b содержит все символы a и ровно одну дополнительную букву.
    test_data = [
        {
            "a": "",
            "b": "a",
            "answer": "a"
        },
        {
            "a": "a",
            "b": "ab",
            "answer": "b"
        },
        {
            "a": "a",
            "b": "aa",
            "answer": "a"
        },
        {
            "a": "abcd",
            "b": "dbeac",
            "answer": "e"
        },
        {
            "a": "abc",
            "b": "zbac",
            "answer": "z"
        },
        {
            "a": "abc",
            "b": "bcad",
            "answer": "d"
        },
        {
            "a": "aabb",
            "b": "babab",
            "answer": "b"
        },
        {
            "a": "aaaa",
            "b": "aaaaa",
            "answer": "a"
        },
        {
            "a": "xyz",
            "b": "zyxx",
            "answer": "x"
        },
        {
            "a": "кот",
            "b": "токр",
            "answer": "р"
        },
        {
            "a": "Aa",
            "b": "aAA",
            "answer": "A"
        },
    ]
    for test_info in test_data:
        result = solution(test_info["a"], test_info["b"])
        err_str = (
            f"\nTest failed for input: "
            f"a={test_info['a']!r}, b={test_info['b']!r}\n"
            f"Expected: {test_info['answer']!r}, but got: {result!r}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Считаем символы строки b в словаре, вычитаем вхождения символов a
    и удаляем нулевые счётчики - остаётся добавленная буква со счётчиком 1.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
