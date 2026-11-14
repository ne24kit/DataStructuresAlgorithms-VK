class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution_smallest(root: TreeNode, k: int) -> int:
    stack = []
    cnt = 0
    curr = root
    while len(stack) > 0 or curr is not None:
        # пушим в стек пока не дойдем до конца слева
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        cnt += 1
        if cnt == k:
            return curr.val

        curr = curr.right # дальше направо перехожу

    return None

def solution_largest(root: TreeNode, k: int) -> int:
    stack = []
    cnt = 0
    curr = root
    while len(stack) > 0 or curr is not None:
        # пушим в стек пока не дойдем до конца справа
        while curr is not None:
            stack.append(curr)
            curr = curr.right

        curr = stack.pop()
        cnt += 1
        if cnt == k:
            return curr.val

        curr = curr.left # дальше налево перехожу

    return None

def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    # Дети узла i находятся на позициях 2*i + 1 и 2*i + 2.
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def test(solution, answer_key):
    test_data = [
        {"nums": [5], "k": 1, "smallest": 5, "largest": 5},
        {"nums": [0], "k": 1, "smallest": 0, "largest": 0},
        {"nums": [2, 1], "k": 1, "smallest": 1, "largest": 2},
        {"nums": [2, 1], "k": 2, "smallest": 2, "largest": 1},
        {"nums": [1, None, 2], "k": 1, "smallest": 1, "largest": 2},
        {"nums": [1, None, 2], "k": 2, "smallest": 2, "largest": 1},
        {"nums": [4, 2, 6, 1, 3, 5, 7], "k": 1, "smallest": 1, "largest": 7},
        {"nums": [4, 2, 6, 1, 3, 5, 7], "k": 2, "smallest": 2, "largest": 6},
        {"nums": [4, 2, 6, 1, 3, 5, 7], "k": 4, "smallest": 4, "largest": 4},
        {"nums": [4, 2, 6, 1, 3, 5, 7], "k": 7, "smallest": 7, "largest": 1},
        {"nums": [5, 3, 8, None, 4, 6, 9], "k": 3, "smallest": 5, "largest": 6},
        {"nums": [5, 3, 8, None, 4, 6, 9], "k": 5, "smallest": 8, "largest": 4},
        {"nums": [3, 2, None, 1], "k": 2, "smallest": 2, "largest": 2},
        {"nums": [1, None, 2, None, None, None, 3], "k": 3, "smallest": 3, "largest": 1},
        {"nums": [-3, -5, -1, None, -4], "k": 2, "smallest": -4, "largest": -3},
        {"nums": [0, -2, 3, -4, -1, 1, 5], "k": 3, "smallest": -1, "largest": 1},
    ]
    for test_info in test_data:
        root = build_tree(test_info["nums"])
        result = solution(root, test_info["k"])
        err_str = (
            f"\n{solution.__name__}: Test failed for input: "
            f"nums={test_info['nums']}, k={test_info['k']}\n"
            f"Expected: {test_info[answer_key]}, but got: {result}"
        )
        assert result == test_info[answer_key], err_str


def answer_on_question():
    ans = """
        просто спускаюсь для минимума в левую ветку O(H) (log N ~ H  если сбалансированное)
        и потом поднимаюсь k раз ну это O(K)
        крч:  O(K + H) для макс аналогично 
    """
    print(ans)


if __name__ == "__main__":
    test(solution_smallest, "smallest")
    test(solution_largest, "largest")
    answer_on_question()
