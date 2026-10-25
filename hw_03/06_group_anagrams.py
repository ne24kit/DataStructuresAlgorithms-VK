def solution(strs: list[str]) -> list[list[str]]:
    hash_table = {}
    for str_ in strs:
        str_sorted = "".join(sorted(str_))
        if str_sorted not in hash_table:
            hash_table[str_sorted] = [str_]
        else:
            hash_table[str_sorted].append(str_)
    
    return list(hash_table.values())


def test():
    test_data = [
        {
            "strs": ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
            "answer": [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
        },
        {
            "strs": [],
            "answer": []
        },
        {
            "strs": [''],
            "answer": [['']]
        },
        {
            "strs": ['', ''],
            "answer": [['', '']]
        },
        {
            "strs": ['a'],
            "answer": [['a']]
        },
        {
            "strs": ['abc', 'bca', 'cab'],
            "answer": [['abc', 'bca', 'cab']]
        },
        {
            "strs": ['a', 'b', 'c'],
            "answer": [['a'], ['b'], ['c']]
        },
        {
            "strs": ['ab', 'ab', 'ba'],
            "answer": [['ab', 'ab', 'ba']]
        },
        {
            "strs": ['aab', 'aba', 'abb', 'bba'],
            "answer": [['aab', 'aba'], ['abb', 'bba']]
        },
        {
            "strs": ['a', 'aa', 'aaa'],
            "answer": [['a'], ['aa'], ['aaa']]
        },
        {
            "strs": ['', 'a', ''],
            "answer": [['', ''], ['a']]
        },
    ]
    for test_info in test_data:
        result = solution(test_info["strs"].copy())
        err_str = (
            f"\nTest failed for input: strs={test_info['strs']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        # Сортировка только в тесте: сравниваем группы без учёта порядка.
        normalized_result = sorted(sorted(group) for group in result)
        normalized_answer = sorted(sorted(group) for group in test_info["answer"])
        assert normalized_result == normalized_answer, err_str



def answer_on_question():
    ans = """
    У анаграмм после сортировки букв получается одинаковый ключ,
    поэтому словарь сразу объединяет их в группы без сравнения каждого слова со всеми.
    Основные затраты - сортировка букв: O(n * k log k),
    где n - количество слов, k - максимальная длина слова.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
