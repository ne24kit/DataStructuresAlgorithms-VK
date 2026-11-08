class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(nums: list[int | None]) -> int | None:
    if len(nums) == 0 or nums[0] is None:
        return None
    
    min_idx = 0
    max_idx = 0

    while min_idx < len(nums):
        new_min_idx = 2 * min_idx + 1
        if new_min_idx >= len(nums) or nums[new_min_idx] is None:
            break
        min_idx = new_min_idx
    while max_idx < len(nums):
        new_max_idx = 2 * max_idx + 2
        if new_max_idx >= len(nums) or nums[new_max_idx] is None:
            break
        max_idx = new_max_idx


    return nums[min_idx] * nums[max_idx]


def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def test():
    test_data = [
        {"nums": [], "answer": None},
        {"nums": [None], "answer": None},
        {"nums": [5], "answer": 25},
        {"nums": [0], "answer": 0},
        {"nums": [-3], "answer": 9},
        {"nums": [2, 1, 3], "answer": 3},
        {"nums": [4, 2, 6, 1, 3, 5, 7], "answer": 7},
        {"nums": [3, 2, None, 1], "answer": 3},
        {"nums": [1, None, 2, None, None, None, 3], "answer": 3},
        {"nums": [0, -3, 5, -7, -1, 2, 9], "answer": -63},
        {"nums": [-4, -6, -2, -8, -5, -3, -1], "answer": 8},
        {"nums": [2, 0, 4], "answer": 0},
        {"nums": [10, 5, 20, None, 7, 15], "answer": 100},
    ]
    for test_info in test_data:
        result = solution(test_info["nums"].copy())
        err_str = (
            f"\nTest failed for input: nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    В BST меньшие значения находятся слева, большие - справа, поэтому минимум
    ищем по левым детям до конца, а максимум - по правым.
    Каждый путь не длиннее высоты дерева h, поэтому оба поиска вместе занимают O(h).
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
