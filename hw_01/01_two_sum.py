

def solution(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    while right > left:
        sum_ = nums[left] + nums[right]
        if sum_ == target:
            return [left, right]
        elif sum_ > target:
            right -= 1
        elif sum_ < target:
            left  += 1
    return []


def test():
    test_data = [
        {
            "nums": [0, 1, 3, 5, 6, 7, 12, 15],
            "target": 11,
            "answer": [3, 4]
        },
        {
            "nums": [-10, -3, 3, 5, 6, 7, 67, 100],
            "target": 0,
            "answer": [1, 2]
        },
        {
            "nums": [3, 8, 9, 11, 16, 18, 19, 21],
            "target": 25,
            "answer": [2, 4]
        },
        {
            "nums": [-2, -1, 0, 1, 2, 3, 5],
            "target": 8,
            "answer": [5, 6]
        },
        {
            "nums": [-2, -1, 0, 1, 2, 3, 5],
            "target": -3,
            "answer": [0, 1]
        },
        {
            "nums": [-11, -2, 0, 1, 2, 3, 5],
            "target": 1,
            "answer": [1, 5]
        },
    ]
    for test_info in test_data:
        result = solution(test_info["nums"], test_info["target"])
        err_str = f"""\nTest failed for input: {test_info['nums']}""" \
                  f""" with target: {test_info['target']}\n""" \
                  f"""Expected: {test_info['answer']}, but got: {result}"""
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()
