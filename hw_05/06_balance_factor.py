class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = None


def solution(root: TreeNode | None) -> None:
    if root is None:
        return root
    def dfs(root):
        if root is None:
            return 0
        l_h = dfs(root.left)
        r_h = dfs(root.right)
        root.balance_factor = l_h -  r_h
        return 1 + max(l_h, r_h)
    dfs(root)
    return root

def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def test():
    test_data = [
        {"nums": [], "answer": {}},
        {"nums": [None], "answer": {}},
        {"nums": [5], "answer": {5: 0}},
        {"nums": [0], "answer": {0: 0}},
        {"nums": [2, 1], "answer": {2: 1, 1: 0}},
        {"nums": [1, None, 2], "answer": {1: -1, 2: 0}},
        {"nums": [2, 1, 3], "answer": {2: 0, 1: 0, 3: 0}},
        {"nums": [3, 2, None, 1], "answer": {3: 2, 2: 1, 1: 0}},
        {"nums": [1, None, 2, None, None, None, 3], "answer": {1: -2, 2: -1, 3: 0}},
        {"nums": [3, 1, None, None, 2], "answer": {3: 2, 1: -1, 2: 0}},
        {"nums": [1, None, 3, None, None, 2], "answer": {1: -2, 3: 1, 2: 0}},
        {"nums": [4, 2, 6, 1, 3, 5, 7], "answer": {4: 0, 2: 0, 6: 0, 1: 0, 3: 0, 5: 0, 7: 0}},
        {"nums": [4, 2, 6, 1], "answer": {4: 1, 2: 1, 6: 0, 1: 0}},
        {"nums": [4, 2, 6, None, None, 5, 7], "answer": {4: -1, 2: 0, 6: 0, 5: 0, 7: 0}},
        {"nums": [4, 2, 6, 1, None, None, 7], "answer": {4: 0, 2: 1, 6: -1, 1: 0, 7: 0}},
        {"nums": [-2, -3, 0, None, None, -1], "answer": {-2: -1, -3: 0, 0: 1, -1: 0}},
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

        solution(root)
        for node, val, left, right in nodes:
            expected = test_info["answer"][val]
            err_str = (
                f"\nTest failed for input: nums={test_info['nums']}, node={val}\n"
                f"Expected: {expected}, but got: {node.balance_factor}"
            )
            assert node.balance_factor == expected, err_str
            assert node.val == val, "Node value was modified"
            assert node.left is left and node.right is right, "Tree structure was modified"


def answer_on_question():
    ans = """
    Сначала считаю высоты детей, потом высоту узла:
    1 + max(высота слева, высота справа). Для None высота 0.
    В balance_factor пишу высоту слева минус высоту справа.
    Каждый узел обхожу один раз: время O(N), память O(H) на рекурсию.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
