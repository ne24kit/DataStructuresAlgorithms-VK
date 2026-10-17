class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def test():
    test_data = [
        {
            "head": [1, 2, 3, 4, 5],
            "answer": [5, 4, 3, 2, 1]
        },
        {
            "head": [1, 2],
            "answer": [2, 1]
        },
        {
            "head": [1],
            "answer": [1]
        },
        {
            "head": [],
            "answer": []
        },
        {
            "head": [-3, 0, 7, -1],
            "answer": [-1, 7, 0, -3]
        },
        {
            "head": [2, 2, 3, 2],
            "answer": [2, 3, 2, 2]
        }
    ]
    for test_info in test_data:
        
        head = None
        for val in test_info["head"][::-1]:
            head = ListNode(val, head)

        res_head = solution(head)
        result = []

        while res_head:
            result.append(res_head.val)
            res_head = res_head.next

        err_str = (
            f"\nTest failed for input: "
            f"head={test_info['head']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()

