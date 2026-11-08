class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    def dfs(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        
        return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
    return dfs(root1, root2)
        

def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def test():
    test_data = [
        {
            "tree1": [],
            "tree2": [],
            "answer": True
        },
        {
            "tree1": [],
            "tree2": [1],
            "answer": False
        },
        {
            "tree1": [1],
            "tree2": [],
            "answer": False
        },
        {
            "tree1": [None],
            "tree2": [],
            "answer": True
        },
        {
            "tree1": [1],
            "tree2": [1],
            "answer": True
        },
        {
            "tree1": [1],
            "tree2": [2],
            "answer": False
        },
        {
            "tree1": [1, 2, 3],
            "tree2": [1, 2, 3],
            "answer": True
        },
        {
            "tree1": [1, 2],
            "tree2": [1, None, 2],
            "answer": False
        },
        {
            "tree1": [1, 2, 3],
            "tree2": [1, 3, 2],
            "answer": False
        },
        {
            "tree1": [1, 2, 3, 4],
            "tree2": [1, 2, 3, 5],
            "answer": False
        },
        {
            "tree1": [1, 2, 3, 4],
            "tree2": [1, 2, 3],
            "answer": False
        },
        {
            "tree1": [1, None, 2, None, None, 3],
            "tree2": [1, None, 2, None, None, 3],
            "answer": True
        },
        {
            "tree1": [0, -2, 3],
            "tree2": [0, -2, 3],
            "answer": True
        },
        {
            "tree1": [1, 1, 1, 1],
            "tree2": [1, 1, 1, None, 1],
            "answer": False
        },
    ]
    for test_info in test_data:
        root1 = build_tree(test_info["tree1"])
        root2 = build_tree(test_info["tree2"])
        result = solution(root1, root2)
        err_str = (
            f"\nTest failed for input: "
            f"tree1={test_info['tree1']}, tree2={test_info['tree2']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Деревья одинаковы, если оба пустые либо значения корней совпадают
    и рекурсивно совпадают их левые и правые поддеревья,
    если узел есть только в одном дереве, структура различается.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
