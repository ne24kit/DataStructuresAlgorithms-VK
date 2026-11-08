from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(nums: list[int | None], idx: int) -> TreeNode | None:
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = solution(nums, 2*idx + 1)
    root.right = solution(nums, 2*idx + 2)
    return root


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []

    res = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            res.append(None)
        else:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    while len(res) != 0 and res[-1] is None:
        res.pop()

    return res




def test():
    test_data = [
        {"nums": [], "answer": []},
        {"nums": [None], "answer": []},
        {"nums": [1], "answer": [1]},
        {"nums": [0], "answer": [0]},
        {"nums": [1, 2, 3], "answer": [1, 2, 3]},
        {"nums": [1, 2], "answer": [1, 2]},
        {"nums": [1, None, 2], "answer": [1, None, 2]},
        {"nums": [1, None, 2, None, None, 3], "answer": [1, None, 2, 3]},
        {"nums": [1, 2, None, 3], "answer": [1, 2, None, 3]},
        {"nums": [1, 2, 3, 4, 5, 6, 7], "answer": [1, 2, 3, 4, 5, 6, 7]},
        {"nums": [1, 2, 3, None, 4, None, 5], "answer": [1, 2, 3, None, 4, None, 5]},
        {"nums": [-1, 0, -2], "answer": [-1, 0, -2]},
        {"nums": [2, 2, 2], "answer": [2, 2, 2]},
        {"nums": [1, 2, None, None, None], "answer": [1, 2]},
    ]
    for test_info in test_data:
        root = solution(test_info["nums"].copy(), 0)
        result = tree_to_list(root)
        err_str = (
            f"\nTest failed for input: nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Для родителя с индексом i левый ребёнок находится на 2*i + 1, правый на 2*i + 2
    Рекурсивно создаём объекты TreeNode и связываем их через left и right
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
