import heapq

# проверку от дураков на k делать впдалу
def solution_smallest(nums: list[int], k: int) -> int:
    heapq.heapify(nums)
    cnt = 0
    while len(nums) > 0 :
        elem = heapq.heappop(nums)
        cnt += 1 
        if cnt == k:
            return elem

    return None
# heapq.heapify_max и heapq.heappop_max появились только в Python 3.14.
# у меня 3.12 пожэтому я буду юзать миинусыы
def solution_largest(nums: list[int], k: int) -> int:
    for i in range(len(nums)):
        nums[i] = -nums[i]

    heapq.heapify(nums)
    cnt = 0
    while len(nums) > 0 :
        elem = heapq.heappop(nums)
        cnt += 1 
        if cnt == k:
            return -elem
    return None
    

def test(solution, answer_key):
    test_data = [
        {"nums": [5], "k": 1, "smallest": 5, "largest": 5},
        {"nums": [0], "k": 1, "smallest": 0, "largest": 0},
        {"nums": [2, 1], "k": 1, "smallest": 1, "largest": 2},
        {"nums": [2, 1], "k": 2, "smallest": 2, "largest": 1},
        {"nums": [3, 1, 5, 2, 4], "k": 1, "smallest": 1, "largest": 5},
        {"nums": [3, 1, 5, 2, 4], "k": 2, "smallest": 2, "largest": 4},
        {"nums": [3, 1, 5, 2, 4], "k": 3, "smallest": 3, "largest": 3},
        {"nums": [3, 1, 5, 2, 4], "k": 5, "smallest": 5, "largest": 1},
        {"nums": [1, 2, 3, 4], "k": 2, "smallest": 2, "largest": 3},
        {"nums": [4, 3, 2, 1], "k": 2, "smallest": 2, "largest": 3},
        {"nums": [1, 1, 3], "k": 2, "smallest": 1, "largest": 1},
        {"nums": [2, 1, 2, 3, 3], "k": 2, "smallest": 2, "largest": 3},
        {"nums": [7, 7, 7, 7], "k": 3, "smallest": 7, "largest": 7},
        {"nums": [-5, -1, -3, -2], "k": 2, "smallest": -3, "largest": -2},
        {"nums": [-2, 0, 5, -1, 0], "k": 2, "smallest": -1, "largest": 0},
        {"nums": [0, 0, 0], "k": 3, "smallest": 0, "largest": 0},
    ]
    for test_info in test_data:
        nums = test_info["nums"].copy()
        result = solution(nums, test_info["k"])
        err_str = (
            f"\n{solution.__name__}: Test failed for input: "
            f"nums={test_info['nums']}, k={test_info['k']}\n"
            f"Expected: {test_info[answer_key]}, but got: {result}"
        )
        assert result == test_info[answer_key], err_str


def answer_on_question():
    ans = """
    Юзаю heapify O(N) и попаю минимум K раз, последний — ответ.
    Для K-го наибольшего сначала меняю знаки прямо в массиве,
    а при возврате меняю знак обратно.
    По времени O(N + K log N) (попаем за O(log N) K раз), по доп. памяти O(1).
    Исходный массив изменяется.
    """
    print(ans)


if __name__ == "__main__":
    test(solution_smallest, "smallest")
    test(solution_largest, "largest")
    answer_on_question()
