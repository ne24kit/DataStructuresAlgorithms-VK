def solution(nums: list[int], target: int) -> list[int]:

    hash_table = {}
    for idx, n in enumerate(nums):
        hash_table[target - n] = idx

    for idx, n in enumerate(nums):
        if n in hash_table and hash_table[n] != idx:
            return [idx, hash_table[n]]
    
    return []


def test():
    test_data = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "answer": [0, 1]
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "answer": [1, 2]
        },
        {
            "nums": [3, 3],
            "target": 6,
            "answer": [0, 1]
        },
        {
            "nums": [],
            "target": 0,
            "answer": []
        },
        {
            "nums": [3],
            "target": 6,
            "answer": []
        },
        {
            "nums": [1, 2, 4],
            "target": 8,
            "answer": []
        },
        {
            "nums": [5, 1, 9, 3],
            "target": 8,
            "answer": [0, 3]
        },
        {
            "nums": [-3, 4, 3, 90],
            "target": 0,
            "answer": [0, 2]
        },
        {
            "nums": [0, 4, 3, 0],
            "target": 0,
            "answer": [0, 3]
        },
        {
            "nums": [-5, -2, -8],
            "target": -10,
            "answer": [1, 2]
        },
        {
            "nums": [1, 5, 1],
            "target": 2,
            "answer": [0, 2]
        },
    ]
    for test_info in test_data:
        result = solution(test_info["nums"].copy(), test_info["target"])
        err_str = (
            f"\nTest failed for input: "
            f"nums={test_info['nums']}, target={test_info['target']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        # Порядок индексов в паре не важен.
        assert sorted(result) == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Для каждого числа ищем target - число среди уже просмотренных в словаре за O(1),
    поэтому второй (внутренний) цикл не нужен и всё решение занимает O(n).
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
