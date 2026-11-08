class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    
    queue = [root]
    res = []
    while len(queue):
        len_ = len(queue)
        res.append(queue[-1].val)
        for i in range(len_):
            if queue[i].left is not None:
                queue.append(queue[i].left)
            if queue[i].right is not None:
                queue.append(queue[i].right)

        queue = queue[len_:]

    return res



def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def test():
    test_data = [
        {"nums": [], "answer": []},
        {"nums": [None], "answer": []},
        {"nums": [1], "answer": [1]},
        {"nums": [0], "answer": [0]},
        {"nums": [1, 2, 3], "answer": [1, 3]},
        {"nums": [1, 2, None, 3], "answer": [1, 2, 3]},
        {"nums": [1, None, 2, None, None, None, 3], "answer": [1, 2, 3]},
        {"nums": [1, 2, 3, None, 5, None, 4], "answer": [1, 3, 4]},
        {"nums": [1, 2, 3, 4, 5], "answer": [1, 3, 5]},
        {"nums": [1, 2, 3, 4, 5, 6, 7], "answer": [1, 3, 7]},
        {"nums": [1, 2, 3, None, None, 4], "answer": [1, 3, 4]},
        {"nums": [-1, -2, -3, -4], "answer": [-1, -3, -4]},
        {"nums": [1, 1, 1, 1], "answer": [1, 1, 1]},
    ]
    for test_info in test_data:
        root = build_tree(test_info["nums"])
        result = solution(root)
        err_str = (
            f"\nTest failed for input: nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Обходим дерево по уровням, добавляя детей слева направо, поэтому последний
    узел в очереди текущего уровня - самый правый; его значение записываем в ответ.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()

