def solution(nums: list[int]) -> list[int]:
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for cur_pos in range(gap, n):
            m_gap = cur_pos
            while m_gap >= gap and nums[m_gap] < nums[m_gap - gap]:
                nums[m_gap], nums[m_gap - gap] = nums[m_gap - gap], nums[m_gap]
                m_gap -= gap
        gap = gap // 2

    return nums 


def test():
    test_data = [
        {
            "nums": [],
            "answer": []
        },
        {
            "nums": [5],
            "answer": [5]
        },
        {
            "nums": [2, 1],
            "answer": [1, 2]
        },
        {
            "nums": [1, 2],
            "answer": [1, 2]
        },
        {
            "nums": [5, 3, 1, 4, 2],
            "answer": [1, 2, 3, 4, 5]
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "answer": [1, 2, 3, 4, 5]
        },
        {
            "nums": [6, 5, 4, 3, 2, 1],
            "answer": [1, 2, 3, 4, 5, 6]
        },
        {
            "nums": [2, 2, 2, 2],
            "answer": [2, 2, 2, 2]
        },
        {
            "nums": [3, 1, 3, 2, 1],
            "answer": [1, 1, 2, 3, 3]
        },
        {
            "nums": [-3, 0, -1, 2, -5],
            "answer": [-5, -3, -1, 0, 2]
        },
        {
            "nums": [0, 0, -1, 1, 0],
            "answer": [-1, 0, 0, 0, 1]
        },
        {
            "nums": [8, 1, 6, 2, 7, 3, 5, 4],
            "answer": [1, 2, 3, 4, 5, 6, 7, 8]
        },
    ]
    for test_info in test_data:
        nums = test_info["nums"].copy()
        result = solution(nums)
        err_str = (
            f"\nTest failed for input: nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str
        assert result is nums, "Функция должна вернуть тот же список, изменённый in-place"


if __name__ == "__main__":
    test()
