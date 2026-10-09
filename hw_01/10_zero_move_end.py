def solution(nums: list[int]) -> list[int]:
    zero_p = 0
    
    for p in range(len(nums)):
        if nums[p] != 0:
            nums[p], nums[zero_p] = nums[zero_p], nums[p]
            zero_p += 1

    return nums            
            

def test():
    test_data = [
        {
            "nums": [0, 0, 1, 0, 3, 12],
            "answer": [1, 3, 12, 0, 0, 0]
        },
        {
            "nums": [0, 33, 57, 88,  60, 0, 0, 80, 99],
            "answer": [33, 57, 88,  60, 80, 99, 0, 0, 0]
        },
        {
            "nums": [0, 0, 0, 18, 16, 0, 0, 77, 99],
            "answer": [18, 16, 77, 99, 0, 0, 0, 0, 0]
        },
        {
            "nums": [],
            "answer": []
        },
        {
            "nums": [0, 0, 0, 0],
            "answer": [0, 0, 0, 0]
        },
        {
            "nums": [5, 2, 9, 1],
            "answer": [5, 2, 9, 1]
        },
        {
            "nums": [3, 1, 2, 0, 0],
            "answer": [3, 1, 2, 0, 0]
        },
    ]
    for test_info in test_data:
        result = solution(test_info["nums"].copy())
        err_str = (
            f"\nTest failed for input: "
            f"nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()
