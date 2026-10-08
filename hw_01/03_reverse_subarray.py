def reverse_array(nums: list[int], left:int, right:int) -> list[int]:
    if right < 1:
        return nums
    
    if left >= right:
        return nums
    
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left  += 1
        right -= 1

    return nums

def solution(nums: list[int], k: int) -> list[int]:
    if k < 1:
        return nums

    n = len(nums)

    if n < 1:
        return nums
    
    k = k % n

    if k == 0:
        return nums

    reverse_array(nums, 0, n - 1)
    reverse_array(nums, 0, k - 1)
    reverse_array(nums, k, n - 1)

    return nums


def test():
    test_data = [
        {
            "nums": [1, 2, 3, 4, 5, 6, 7],
            "k": 3,
            "answer": [5, 6, 7, 1, 2, 3, 4]
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 0,
            "answer": [1, 2, 3, 4, 5]
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 1,
            "answer": [5, 1, 2, 3, 4]
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 4,
            "answer": [2, 3, 4, 5, 1]
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 5,
            "answer": [1, 2, 3, 4, 5]
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 10,
            "answer": [1, 2, 3, 4, 5]
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 7,
            "answer": [4, 5, 1, 2, 3]
        },
        {
            "nums": [1, 2, 3],
            "k": 10**9,
            "answer": [3, 1, 2]
        },
        {
            "nums": [1, 2, 3, 4],
            "k": 2,
            "answer": [3, 4, 1, 2]
        },
        {
            "nums": [1, 2],
            "k": 1,
            "answer": [2, 1]
        },
        {
            "nums": [67],
            "k": 100,
            "answer": [67]
        },
        {
            "nums": [-3, -2, -1, 0, 1],
            "k": 2,
            "answer": [0, 1, -3, -2, -1]
        },
        {
            "nums": [1, 2, 1, 2, 3],
            "k": 2,
            "answer": [2, 3, 1, 2, 1]
        },
        {
            "nums": [7, 7, 7, 7],
            "k": 3,
            "answer": [7, 7, 7, 7]
        },
        {
            "nums": [],
            "k": 0,
            "answer": []
        },
        {
            "nums": [],
            "k": 3,
            "answer": []
        },
    ]
    for test_info in test_data:
        result = solution(test_info["nums"].copy(), test_info["k"])
        err_str = (
            f"\nTest failed for input: {test_info['nums']}, k={test_info['k']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()
