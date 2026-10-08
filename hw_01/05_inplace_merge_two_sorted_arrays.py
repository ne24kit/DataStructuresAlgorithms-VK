def solution(arr1: list[int], arr2: list[int]) -> list[int]:
    pointer_3 = len(arr1) - 1
    pointer_2 = len(arr2) - 1
    pointer_1 = pointer_3 - pointer_2 - 1

    while pointer_2 >= 0:
        if pointer_1 >= 0 and arr1[pointer_1] > arr2[pointer_2]:
            arr1[pointer_3] = arr1[pointer_1]
            pointer_1 -= 1
        else:
            arr1[pointer_3] = arr2[pointer_2]
            pointer_2 -= 1
        
        pointer_3 -= 1
    return arr1

    
def test():
    test_data = [
        {
            "arr1": [3, 8, 10, 11, 0, 0, 0],
            "arr2": [1, 7, 9],
            "answer": [1, 3, 7, 8, 9, 10, 11]
        },
        {
            "arr1": [1, 3, 5, 0, 0, 0],
            "arr2": [2, 4, 6],
            "answer": [1, 2, 3, 4, 5, 6]
        },
        {
            "arr1": [],
            "arr2": [],
            "answer": []
        },
        {
            "arr1": [1, 2, 3],
            "arr2": [],
            "answer": [1, 2, 3]
        },
        {
            "arr1": [1, 0],
            "arr2": [2],
            "answer": [1, 2]
        },
        {
            "arr1": [2, 0],
            "arr2": [1],
            "answer": [1, 2]
        },
        {
            "arr1": [1, 0],
            "arr2": [1],
            "answer": [1, 1]
        },
        {
            "arr1": [1, 2, 3, 0, 0, 0],
            "arr2": [4, 5, 6],
            "answer": [1, 2, 3, 4, 5, 6]
        },
        {
            "arr1": [4, 5, 6, 0, 0, 0],
            "arr2": [1, 2, 3],
            "answer": [1, 2, 3, 4, 5, 6]
        },
        {
            "arr1": [3, 0, 0, 0, 0, 0],
            "arr2": [1, 2, 4, 5, 6],
            "answer": [1, 2, 3, 4, 5, 6]
        },
        {
            "arr1": [1, 2, 4, 5, 6, 0],
            "arr2": [3],
            "answer": [1, 2, 3, 4, 5, 6]
        },
        {
            "arr1": [1, 1, 3, 5, 0, 0, 0, 0],
            "arr2": [1, 2, 3, 3],
            "answer": [1, 1, 1, 2, 3, 3, 3, 5]
        },
        {
            "arr1": [7, 7, 0, 0, 0],
            "arr2": [7, 7, 7],
            "answer": [7, 7, 7, 7, 7]
        },
        {
            "arr1": [-5, -1, 0, 4, 0, 0, 0, 0],
            "arr2": [-3, 0, 2, 6],
            "answer": [-5, -3, -1, 0, 0, 2, 4, 6]
        },
        {
            "arr1": [-10, -5, -2, 0, 0, 0],
            "arr2": [-8, -3, -1],
            "answer": [-10, -8, -5, -3, -2, -1]
        }
    ]
    for test_info in test_data:
        result = solution(test_info["arr1"].copy(), test_info["arr2"].copy())
        err_str = (
            f"\nTest failed for input: arr1={test_info['arr1']}, "
            f"arr2={test_info['arr2']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()
