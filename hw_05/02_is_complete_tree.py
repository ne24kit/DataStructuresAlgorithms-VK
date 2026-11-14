class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root: TreeNode | None) -> bool:
    if root is None:
        return True
    queue = [root]
    is_last_lvl = False
    while len(queue) > 0:
        len_ = len(queue)
        for i in range(len_):
            if queue[i] is None:
                is_last_lvl = True
            else:
                if is_last_lvl:
                    return False
                queue.append(queue[i].left)
                queue.append(queue[i].right)

        queue = queue[len_:]
    return True
            
    

def build_tree(nums: list[int | None], idx: int = 0) -> TreeNode | None:
    if idx >= len(nums) or nums[idx] is None:
        return None
    root = TreeNode(nums[idx])
    root.left = build_tree(nums, 2 * idx + 1)
    root.right = build_tree(nums, 2 * idx + 2)
    return root


def test():
    test_data = [
        {"nums": [], "answer": True},
        {"nums": [None], "answer": True},
        {"nums": [1], "answer": True},
        {"nums": [0], "answer": True},
        {"nums": [1, 2], "answer": True},
        {"nums": [1, None, 2], "answer": False},
        {"nums": [1, 2, 3], "answer": True},
        {"nums": [1, 2, 3, 4], "answer": True},
        {"nums": [1, 2, 3, 4, 5], "answer": True},
        {"nums": [1, 2, 3, 4, 5, 6], "answer": True},
        {"nums": [1, 2, 3, 4, 5, 6, 7], "answer": True},
        {"nums": [1, 2, 3, 4, 5, 6, 7, 8], "answer": True},
        {"nums": [1, 2, 3, 4, 5, None, 7], "answer": False},
        {"nums": [1, 2, 3, None, 5], "answer": False},
        {"nums": [1, 2, 3, None, None, 6, 7], "answer": False},
        {"nums": [1, 2, None, 4], "answer": False},
        {"nums": [1, 2, 3, 4, None, None, None, 8], "answer": False},
        {"nums": [-1, -2, -3, -4], "answer": True},
        {"nums": [1, 1, 1, 1], "answer": True},
        {"nums": [1, 1, 1, 1, None, 1], "answer": False},
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
    BFS, как только встретил None, ставлю флаг: если дальше будет хоть один 
    узел не None значит этот флаг был про дырку.
    По времени O(n), по памяти O(n) на очередь.
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
