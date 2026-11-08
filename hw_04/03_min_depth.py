class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode | None) -> int:

    def dfs(left, right):
        if left is None and right is None:
            return 1
        
        if left is None:
            return 1 + dfs(right.left, right.right)

        if right is None:
            return 1 + dfs(left.left, left.right)

        return 1 + min(
            dfs(left.left, left.right),
            dfs(right.left, right.right)
        )

    if root is None:
        return 0 
    return dfs(root.left, root.right)
    
    


def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    # Дети узла i находятся на позициях 2*i + 1 и 2*i + 2.
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def test():
    test_data = [
        {"nums": [], "answer": 0},
        {"nums": [None], "answer": 0},
        {"nums": [1], "answer": 1},
        {"nums": [0], "answer": 1},
        {"nums": [1, 2], "answer": 2},
        {"nums": [1, None, 2], "answer": 2},
        {"nums": [1, 2, 3], "answer": 2},
        {"nums": [1, 2, None, 3], "answer": 3},
        {"nums": [1, None, 2, None, None, None, 3], "answer": 3},
        {"nums": [1, 2, 3, 4], "answer": 2},
        {"nums": [1, 2, 3, None, None, 4, 5], "answer": 2},
        {"nums": [1, 2, 3, 4, 5, 6, 7], "answer": 3},
        {"nums": [-1, -2, -3], "answer": 2},
        {"nums": [1, 1, None, 1], "answer": 3},
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
    BFS обходит дерево по уровням от корня, поэтому первый 
    встреченный лист(узел без обоих детей) находится на минимальной глубине
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
