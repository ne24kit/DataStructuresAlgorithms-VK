def solution(nums: list[int]) -> list[int]:
    left = 0 
    mid = 0
    right = len(nums) - 1

    if right < 0:
        return nums
    
    while mid <= right:
        if nums[mid] == 2:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
        elif nums[mid] == 0:
            nums[mid], nums[left] = nums[left], nums[mid]
            left += 1
            mid += 1
        else:
            mid += 1

    return nums            
            

def test():
    test_data = [
        {
            "nums": [],
            "answer": []
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
            "nums": [2],
            "answer": [2]
        },
        {
            "nums": [0, 0, 0, 0],
            "answer": [0, 0, 0, 0]
        },
        {
            "nums": [1, 1, 1, 1],
            "answer": [1, 1, 1, 1]
        },
        {
            "nums": [2, 2, 2, 2],
            "answer": [2, 2, 2, 2]
        },
        {
            "nums": [1, 0],
            "answer": [0, 1]
        },
        {
            "nums": [2, 0],
            "answer": [0, 2]
        },
        {
            "nums": [2, 1],
            "answer": [1, 2]
        },
        {
            "nums": [0, 1, 2],
            "answer": [0, 1, 2]
        },
        {
            "nums": [0, 2, 1],
            "answer": [0, 1, 2]
        },
        {
            "nums": [1, 0, 2],
            "answer": [0, 1, 2]
        },
        {
            "nums": [1, 2, 0],
            "answer": [0, 1, 2]
        },
        {
            "nums": [2, 0, 1],
            "answer": [0, 1, 2]
        },
        {
            "nums": [2, 1, 0],
            "answer": [0, 1, 2]
        },
        {
            "nums": [0, 0, 1, 1, 2, 2],
            "answer": [0, 0, 1, 1, 2, 2]
        },
        {
            "nums": [2, 2, 1, 1, 0, 0],
            "answer": [0, 0, 1, 1, 2, 2]
        },
        {
            "nums": [1, 0, 1, 0, 1, 0],
            "answer": [0, 0, 0, 1, 1, 1]
        },
        {
            "nums": [2, 0, 2, 0, 2, 0],
            "answer": [0, 0, 0, 2, 2, 2]
        },
        {
            "nums": [2, 1, 2, 1, 2, 1],
            "answer": [1, 1, 1, 2, 2, 2]
        },
        {
            "nums": [2, 0, 2, 1, 1, 0],
            "answer": [0, 0, 1, 1, 2, 2]
        },
        {
            "nums": [2, 0, 2, 2, 1, 0, 2],
            "answer": [0, 0, 1, 2, 2, 2, 2]
        },
        {
            "nums": [1, 1, 1, 0],
            "answer": [0, 1, 1, 1]
        },
        {
            "nums": [2, 0, 1] * 100,
            "answer": [0] * 100 + [1] * 100 + [2] * 100
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
