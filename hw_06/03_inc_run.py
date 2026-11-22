def solution(nums: list[int]) -> int:
    curr_max_len = 1 
    final_max_len = 1 
    if len(nums) < 2:
        return len(nums)

    for i in range(1, len(nums)):
        if  nums[i] > nums[i - 1]:
            curr_max_len += 1 
        else:
            final_max_len = max(final_max_len, curr_max_len)
            curr_max_len = 1

    final_max_len = max(final_max_len, curr_max_len)
    return final_max_len


def test():
    test_data = [
        {"nums": [], "answer": 0},
        {"nums": [5], "answer": 1},
        {"nums": [3, 2, 8, 9, 5, 10], "answer": 3},
        {"nums": [1, 2, 7, 9, 0, 10], "answer": 4},
        {"nums": [8, 8, 8, 8], "answer": 1},
        {"nums": [5, 4, 3, 2, 1], "answer": 1},
        {"nums": [-3, -2, -1, 0], "answer": 4},
        {"nums": [1, 2, 2, 3, 4], "answer": 3},
    ]
    for test_info in test_data:
        nums = test_info["nums"].copy()
        result = solution(nums)
        err_str = (
            f"\nTest failed for input: nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Если число больше предыдущего, увеличиваю текущую длину на 1, 
    иначе обновляю максимум и сбрасываю текущую длину до 1.
    В конце тоже обновляю максимум.
    O(n) время, O(1) память.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
