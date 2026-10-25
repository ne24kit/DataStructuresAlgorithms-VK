def solution(animals: list[int], portions: list[int]) -> int:
    if len(animals) == 0 or len(portions) == 0:
        return 0
    animals = sorted(animals)
    portions = sorted(portions)
    total_animals = len(animals)
    cnt = 0
    for food in portions:
        if food >= animals[cnt]:
            cnt += 1
        if cnt == total_animals:
            break
    return cnt

def test():
    test_data = [
        {
            "animals": [],
            "portions": [],
            "answer": 0
        },
        {
            "animals": [],
            "portions": [1, 2],
            "answer": 0
        },
        {
            "animals": [1, 2],
            "portions": [],
            "answer": 0
        },
        {
            "animals": [3],
            "portions": [3],
            "answer": 1
        },
        {
            "animals": [3],
            "portions": [2],
            "answer": 0
        },
        {
            "animals": [3],
            "portions": [5],
            "answer": 1
        },
        {
            "animals": [1, 2, 3],
            "portions": [1, 1],
            "answer": 1
        },
        {
            "animals": [1, 2],
            "portions": [1, 2, 3],
            "answer": 2
        },
        {
            "animals": [4, 2, 3],
            "portions": [3, 1, 4],
            "answer": 2
        },
        {
            "animals": [2, 2, 2],
            "portions": [2, 2],
            "answer": 2
        },
        {
            "animals": [5, 6],
            "portions": [1, 2, 3],
            "answer": 0
        },
        {
            "animals": [3, 1, 2],
            "portions": [2, 3, 1],
            "answer": 3
        },
        {
            "animals": [2, 3],
            "portions": [1, 3],
            "answer": 1
        },
    ]
    for test_info in test_data:
        result = solution(test_info["animals"].copy(), test_info["portions"].copy())
        err_str = (
            f"\nTest failed for input: "
            f"animals={test_info['animals']}, portions={test_info['portions']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Кормим сначала животных с меньшей потребностью 
    самыми маленькими подходящими порциями, 
    сохраняя большие для остальных 
    и получая максимум накормленных животных.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
