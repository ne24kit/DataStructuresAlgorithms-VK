def solution(stack: list[int]) -> list[int]:
    tmp_stack =[]

    while len(stack) > 0:
        curr = stack.pop()
        while len(tmp_stack) > 0  and tmp_stack[-1] > curr:
            stack.append(tmp_stack.pop())
        tmp_stack.append(curr)

    return tmp_stack


def test():
    test_data = [
        {
            "stack": [],
            "answer": []
        },
        {
            "stack": [5],
            "answer": [5]
        },
        {
            "stack": [2, 1],
            "answer": [1, 2]
        },
        {
            "stack": [1, 2],
            "answer": [1, 2]
        },
        {
            "stack": [3, 1, 4, 2],
            "answer": [1, 2, 3, 4]
        },
        {
            "stack": [1, 2, 3, 4],
            "answer": [1, 2, 3, 4]
        },
        {
            "stack": [4, 3, 2, 1],
            "answer": [1, 2, 3, 4]
        },
        {
            "stack": [2, 2, 2],
            "answer": [2, 2, 2]
        },
        {
            "stack": [3, 1, 3, 2, 1],
            "answer": [1, 1, 2, 3, 3]
        },
        {
            "stack": [-3, 0, -1, 2, -5],
            "answer": [-5, -3, -1, 0, 2]
        },
    ]
    for test_info in test_data:
        result = solution(test_info["stack"].copy())
        err_str = (
            f"\nTest failed for input: stack={test_info['stack']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()
