from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode | None) -> TreeNode | None:

    def dfs(root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return root


def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    # Дети узла i находятся на позициях 2*i + 1 и 2*i + 2.
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []
    result = []
    queue = [root]
    idx = 0
    while idx < len(queue):
        node = queue[idx]
        idx += 1
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


def test():
    # nums задаёт позиции детей по индексам; answer — BFS с пропусками,
    # без детей отсутствующих узлов и без None в конце.
    test_data = [
        {"nums": [], "answer": []},
        {"nums": [None], "answer": []},
        {"nums": [1], "answer": [1]},
        {"nums": [0], "answer": [0]},
        {"nums": [1, 2], "answer": [1, None, 2]},
        {"nums": [1, None, 2], "answer": [1, 2]},
        {"nums": [1, 2, 3], "answer": [1, 3, 2]},
        {"nums": [1, 2, 3, 4, 5, 6, 7], "answer": [1, 3, 2, 7, 6, 5, 4]},
        {"nums": [1, 2, 3, 4], "answer": [1, 3, 2, None, None, None, 4]},
        {"nums": [1, 2, 3, None, 5, 6], "answer": [1, 3, 2, None, 6, 5]},
        {"nums": [1, 2, None, 3], "answer": [1, None, 2, None, 3]},
        {"nums": [1, None, 2, None, None, None, 3], "answer": [1, 2, None, 3]},
        {"nums": [1, 2, None, None, 3], "answer": [1, None, 2, 3]},
        {"nums": [-1, -2, -3], "answer": [-1, -3, -2]},
        {"nums": [1, 1, 1, 1], "answer": [1, 1, 1, None, None, None, 1]},
    ]
    for test_info in test_data:
        root = build_tree(test_info["nums"])
        nodes = []
        stack = [root] if root is not None else []
        while stack:
            node = stack.pop()
            nodes.append((node, node.val, node.left, node.right))
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        result_root = solution(root)
        assert result_root is root, "Expected the original root"
        for node, val, left, right in nodes:
            assert node.val == val, "Node value was modified"
            assert node.left is right and node.right is left, (
                f"Children were not swapped for node={val}, nums={test_info['nums']}"
            )
        result = tree_to_list(result_root)
        err_str = (
            f"\nTest failed for input: nums={test_info['nums']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    У каждого узла меняю местами левого и правого ребёнка.
    Делаю это для всех узлов, поэтому всё дерево становится зеркальным.
    Время O(N): каждый узел посещаю один раз.
    Память O(H) на рекурсию, где H — высота дерева.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
