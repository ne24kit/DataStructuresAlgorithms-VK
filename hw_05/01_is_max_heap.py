def solution(nums: list[int]) -> bool:
    n = len(nums)
    if n < 2:
        return True

    for i in range((n - 2) // 2 + 1):
        if 2 * i + 1 < n and nums[i] < nums[2 * i + 1]:
            return False
        if 2 * i + 2 < n and nums[i] < nums[2 * i + 2]:
            return False
    return True


def test():
    test_data = [
        {"nums": [], "answer": True},
        {"nums": [1], "answer": True},
        {"nums": [0], "answer": True},
        {"nums": [2, 1], "answer": True},
        {"nums": [1, 2], "answer": False},
        {"nums": [3, 2, 1], "answer": True},
        {"nums": [3, 1, 2], "answer": True},
        {"nums": [2, 3, 1], "answer": False},
        {"nums": [2, 1, 3], "answer": False},
        {"nums": [7, 6, 5, 4], "answer": True},
        {"nums": [7, 6, 5, 4, 3], "answer": True},
        {"nums": [7, 6, 5, 4, 3, 2], "answer": True},
        {"nums": [7, 6, 5, 4, 3, 2, 1], "answer": True},
        {"nums": [9, 5, 8, 6, 4], "answer": False},
        {"nums": [9, 8, 5, 4, 3, 6], "answer": False},
        {"nums": [9, 8, 5, 4, 3, 2, 6], "answer": False},
        {"nums": [-1, -2, -3, -4], "answer": True},
        {"nums": [-3, -2, -1], "answer": False},
        {"nums": [0, 0, 0, 0], "answer": True},
        {"nums": [1, 1, 1, 1, 1, 1], "answer": True},
    ]
    for test_info in test_data:
        nums = test_info["nums"].copy()
        result = solution(nums)
        err_str = (
            f"\nTest failed for input: nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str
        assert nums == test_info["nums"], "Input array was modified"


def answer_on_question():
    ans = """
    Крч я вот ограничение: 
    ласт у которого есть сосед -  это 2 * i + 1 = n - 1, то есть i = (n - 2) // 2,  
    а значит давайте мы будем идти только до него и сразу выйдем и не будем чекать последний ряд
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
