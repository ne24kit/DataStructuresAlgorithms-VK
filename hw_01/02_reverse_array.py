def solution(nums: list[int]) -> list[int]:
    
    left = 0 
    right = len(nums) - 1
    if right < 1:
        return nums


    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left  += 1
        right -= 1

    return nums


def test():
    test_data = [
        {
            "nums": [0, 1, 3, 5, 6, 7, 12, 15],
            "answer": [15, 12, 7, 6, 5, 3, 1, 0]
        },
        {
            "nums": [100, 3, 10, -1, 2, 3],
            "answer": [3, 2, -1, 10, 3, 100]
        },
        {
            "nums": [0, 1, 2, 3],
            "answer": [3, 2, 1, 0]
        },
        {
            "nums": [0, 1],
            "answer": [1, 0]
        },
        {
            "nums": [1],
            "answer": [1]
        },
        {
            "nums": [],
            "answer": []
        },
        {
            "nums": [i for i in range(0, 10000)],
            "answer": [i for i in range(10000 - 1, -1, -1)]
        },
        {
            "nums": [i for i in range(-100, 100)],
            "answer": [i for i in range(100 - 1, -100 - 1, -1)]
        },
    ]
    for test_info in test_data:
        result = solution(test_info["nums"])
        err_str = f"""\nTest failed for input: {test_info['nums']}""" \
                  f"""Expected: {test_info['answer']}, but got: {result}"""
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()


    