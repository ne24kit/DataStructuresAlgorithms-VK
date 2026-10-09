def solution(target: int, nums: list[int]) -> int:
    left = 0 
    len_ = len(nums)
    min_len = len_ + 1
    cur_sum = 0
    right = 0
    while right < len_ or left <= right:
        if cur_sum >= target:
            min_len = min(right - left, min_len)
            cur_sum -= nums[left]
            left += 1
        else:
            if right == len_:
                break
            cur_sum += nums[right]
            right += 1

    return 0 if min_len == len_ + 1 else min_len

def test():
    test_data = [
        {
            "target": 7,
            "nums": [2, 3, 1, 2, 4, 3],
            "answer": 2
        },
        {
            "target": 4,
            "nums": [1, 4, 4],
            "answer": 1
        },
        {
            "target": 11,
            "nums": [1, 1, 1, 1, 1, 1, 1, 1],
            "answer": 0
        },
        {
            "target": 1,
            "nums": [1],
            "answer": 1
        },
        {
            "target": 3,
            "nums": [5],
            "answer": 1
        },
        {
            "target": 5,
            "nums": [3],
            "answer": 0
        },
        {
            "target": 7,
            "nums": [3, 4],
            "answer": 2
        },
        {
            "target": 6,
            "nums": [3, 4],
            "answer": 2
        },
        {
            "target": 10,
            "nums": [1, 2, 3, 4],
            "answer": 4
        },
        {
            "target": 9,
            "nums": [2, 2, 2, 4],
            "answer": 4
        },
        {
            "target": 7,
            "nums": [7, 1, 1, 1],
            "answer": 1
        },
        {
            "target": 7,
            "nums": [1, 1, 8, 1],
            "answer": 1
        },
        {
            "target": 7,
            "nums": [1, 1, 1, 7],
            "answer": 1
        },
        {
            "target": 8,
            "nums": [4, 5, 1, 1, 1],
            "answer": 2
        },
        {
            "target": 9,
            "nums": [1, 4, 5, 1],
            "answer": 2
        },
        {
            "target": 9,
            "nums": [1, 1, 1, 4, 5],
            "answer": 2
        },
        {
            "target": 11,
            "nums": [2, 2, 2, 2, 7],
            "answer": 3
        },
        {
            "target": 8,
            "nums": [3, 3, 3, 3],
            "answer": 3
        },
    ]
    for test_info in test_data:
        result = solution(test_info["target"], test_info["nums"].copy())
        err_str = (
            f"\nTest failed for input: "
            f"target={test_info['target']},"
            f"nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()
