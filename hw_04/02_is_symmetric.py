class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution_bfs(root: TreeNode | None) -> bool:
    queue = [root]
    while len(queue):
        len_ = len(queue)
        for i in range(len_):
            if queue[i] is None and queue[len_ -1 - i] is None:
                continue
            if queue[i] is None or queue[len_ -1 - i] is None:
                return False
            if queue[i].val != queue[len_ -1 - i].val:
                return False
            queue.append(queue[i].left)
            queue.append(queue[i].right)
        queue = queue[len_:]
    return True

def solution_dfs(root: TreeNode | None) -> bool:
    if root is None:
        return True
    def dfs(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False

        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)
    

def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def test(solution):
    test_data = [
        {"nums": [], "answer": True},
        {"nums": [None], "answer": True},
        {"nums": [1], "answer": True},
        {"nums": [1, 2, 2], "answer": True},
        {"nums": [1, 2, 3], "answer": False},
        {"nums": [1, 2], "answer": False},
        {"nums": [1, None, 2], "answer": False},
        {"nums": [1, 2, 2, 3, 4, 4, 3], "answer": True},
        {"nums": [1, 2, 2, None, 3, 3, None], "answer": True},
        {"nums": [1, 2, 2, None, 3, None, 3], "answer": False},
        {"nums": [1, 2, 2, 3, 4, 4, 5], "answer": False},
        {"nums": [0, -1, -1, -2, None, None, -2], "answer": True},
        {"nums": [1, 1, 1, 1, None, None, 1], "answer": True},
        {"nums": [1, 1, 1, 1, None, 1, None], "answer": False},
    ]
    for test_info in test_data:
        root = build_tree(test_info["nums"])
        result = solution(root)
        err_str = (
            f"\n{solution.__name__}: Test failed for input: nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    BFS: на каждом уровне сравниваем узлы с противоположных концов очереди.
    DFS: рекурсивно сравниваем left.left с right.right и left.right с right.left.
    В обоих решениях значения зеркальных узлов должны совпадать,
    а отсутствующие узлы - находиться в паре, поэтому проверяем и значения, и структуру.
    """
    print(ans)


if __name__ == "__main__":
    test(solution_bfs)
    test(solution_dfs)
    answer_on_question()
