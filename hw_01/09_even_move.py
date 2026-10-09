def solution(nums: list[int]) -> list[int]:
    even_p = 0
    
    for p in range(len(nums)):
        if nums[p] % 2 == 0:
            nums[p], nums[even_p] = nums[even_p], nums[p]
            even_p += 1

    return nums            
            

def test():
    test_data = [
        {
            "nums": [3, 2, 4, 1, 11, 8, 9],
            "answer": [2, 4, 8, 1, 11, 3, 9]
        },
        {
            "nums": [],
            "answer": []
        },
        {
            "nums": [2],
            "answer": [2]
        },
        {
            "nums": [-2],
            "answer": [-2]
        },
        {
            "nums": [8, 2, 6, 4],
            "answer": [8, 2, 6, 4]
        },
        {
            "nums": [7, 3, 9, 1],
            "answer": [7, 3, 9, 1]
        },
        {
            "nums": [3, 2],
            "answer": [2, 3]
        },
        {
            "nums": [2, 3],
            "answer": [2, 3]
        },
        {
            "nums": [1, 2, 3, 4, 5, 6],
            "answer": [2, 4, 6, 1, 3, 5]
        },
        {
            "nums": [2, 1, 4, 3, 6, 5],
            "answer": [2, 4, 6, 1, 3, 5]
        },
        {
            "nums": [1, 3, 5, 2],
            "answer": [2, 1, 3, 5]
        },
        {
            "nums": [3, 8, 2, 6, 1],
            "answer": [8, 2, 6, 3, 1]
        },
        {
            "nums": [3, 2, 3, 4, 2, 1, 4],
            "answer": [2, 4, 2, 4, 3, 3, 1]
        },
        {
            "nums": list(range(10000)),
            "answer": list(range(0, 10000, 2)) + list(range(1, 10000, 2))
        },
    ]
    for test_info in test_data:
        result = solution(test_info["nums"].copy())
        even_count = sum(num % 2 == 0 for num in test_info["nums"])
        err_str = (
            f"\nTest failed for input: "
            f"nums={test_info['nums']}\n"
            f"Expected even prefix: {test_info['answer'][:even_count]}\n"
            f"Expected odd elements (any order): {test_info['answer'][even_count:]}\n"
            f"Got: {result}"
        )
        assert result[:even_count] == test_info["answer"][:even_count], err_str
        assert sorted(result[even_count:]) == sorted(test_info["answer"][even_count:]), err_str


if __name__ == "__main__":
    test()
