

def solution(nums: list[int]) -> int:
    slow = 0
    if not nums:
        return 0

    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        else:
            fast += 1

    return slow + 1


def test():
    test_data = [
        {
            "nums": [1, 1, 2],
            "answer": [1, 2]
        },
        {
            "nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            "answer": [0, 1, 2, 3, 4]
        },
        {
            "nums": [3],
            "answer": [3]
        },
        {
            "nums": [2, 2, 2, 2],
            "answer": [2]
        },
        {
            "nums": [1, 2, 3],
            "answer": [1, 2, 3]
        },
        {
            "nums": [-3, -3, -1, 0, 0, 2],
            "answer": [-3, -1, 0, 2]
        },
        {
            "nums": [1, 1, 2, 3, 3],
            "answer": [1, 2, 3]
        },
        {
            "nums": [],
            "answer": []
        },
    ]
    for test_info in test_data:
        nums = test_info["nums"].copy()
        result = solution(nums)
        err_str = (
            f"\nTest failed for input: nums={test_info['nums']}\n"
            f"Expected: length={len(test_info['answer'])}, nums={test_info['answer']}, "
            f"but got: length={result}, nums={nums[:result]}"
        )
        assert result == len(test_info["answer"]), err_str
        assert nums[:result] == test_info["answer"], err_str


def answer_on_question():
    ans = """
    fast перебирает элементы, slow хранит индекс последнего уникального элемента.
    При новом значении увеличиваем slow и записываем nums[fast] в nums[slow].
    Так уникальные элементы перезаписывают дубликаты в начале того же массива.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
