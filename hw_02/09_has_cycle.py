class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode | None) -> bool:
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


def test():
   
    test_data = [
        {
            "head": [],
            "pos": -1,
            "answer": False
        },
        {
            "head": [1],
            "pos": -1,
            "answer": False
        },
        {
            "head": [1],
            "pos": 0,
            "answer": True
        },
        {
            "head": [1, 2],
            "pos": -1,
            "answer": False
        },
        {
            "head": [1, 2],
            "pos": 0,
            "answer": True
        },
        {
            "head": [3, 2, 0, -4],
            "pos": 1,
            "answer": True
        },
        {
            "head": [1, 2, 3, 4, 5],
            "pos": 0,
            "answer": True
        },
        {
            "head": [1, 2, 3, 4, 5],
            "pos": 4,
            "answer": True
        },
        {
            "head": [1, 2, 3, 4, 5],
            "pos": -1,
            "answer": False
        },
        {
            "head": [2, 2, 2, 2],
            "pos": -1,
            "answer": False
        },
        {
            "head": [2, 2, 2, 2],
            "pos": 2,
            "answer": True
        },
    ]
    for test_info in test_data:
        nodes = [ListNode(val) for val in test_info["head"]]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        if test_info["pos"] != -1:
            nodes[-1].next = nodes[test_info["pos"]]

        head = nodes[0] if nodes else None
        result = solution(head)
        err_str = (
            f"\nTest failed for input: "
            f"head={test_info['head']}, pos={test_info['pos']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()
