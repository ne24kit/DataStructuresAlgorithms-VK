def solution(nums: list[int]) -> list[int]:
    left = 0 
    right = len(nums) - 1

    if right < 0:
        return nums
    
    while left < right:
        if nums[right] == 1:
            right -= 1
        elif nums[left] == 0:
            left += 1
        else:
            nums[left] = 0
            nums[right] = 1
            left += 1
            right -= 1

    return nums            
            

def test():
    test_data = [
        {
            "nums": [0, 1],
            "answer": [0, 1]
        },
        {
            "nums": [1, 0],
            "answer": [0, 1]
        },
        {
            "nums": [0, 0],
            "answer": [0, 0]
        },
        {
            "nums": [1, 1],
            "answer": [1, 1]
        },
        {
            "nums": [0, 0, 1, 0, 1],
            "answer": [0, 0, 0, 1, 1]
        },
        {
            "nums": [1, 0, 1, 0, 1],
            "answer": [0, 0, 1, 1, 1]
        },
        {
            "nums": [0],
            "answer": [0]
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
            "nums": [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            "answer": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        },
        {
            "nums": [1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
            "answer": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        }
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
