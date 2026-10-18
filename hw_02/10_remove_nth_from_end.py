class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode()
    dummy.next = head 
    fast = dummy
    slow = dummy 
    for _ in range(n):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    
    slow.next = slow.next.next

    return dummy.next


def test():
    # Считаем, что 1 <= n <= длина списка.
    test_data = [
        {
            "head": [1, 2, 3, 4, 5],
            "n": 2,
            "answer": [1, 2, 3, 5]
        },
        {
            "head": [1],
            "n": 1,
            "answer": []
        },
        {
            "head": [1, 2],
            "n": 1,
            "answer": [1]
        },
        {
            "head": [1, 2],
            "n": 2,
            "answer": [2]
        },
        {
            "head": [1, 2, 3, 4, 5],
            "n": 5,
            "answer": [2, 3, 4, 5]
        },
        {
            "head": [1, 2, 3, 4, 5],
            "n": 1,
            "answer": [1, 2, 3, 4]
        },
        {
            "head": [1, 2, 3, 4, 5],
            "n": 3,
            "answer": [1, 2, 4, 5]
        },
        {
            "head": [2, 2, 2],
            "n": 2,
            "answer": [2, 2]
        },
        {
            "head": [-3, 0, 7, -1],
            "n": 3,
            "answer": [-3, 7, -1]
        },
    ]
    for test_info in test_data:
        head = None
        for val in test_info["head"][::-1]:
            head = ListNode(val, head)

        res_head = solution(head, test_info["n"])
        result = []
        # Ограничиваем обход, чтобы тест не завис при появлении цикла.
        while res_head is not None and len(result) <= len(test_info["head"]):
            result.append(res_head.val)
            res_head = res_head.next

        err_str = (
            f"\nTest failed for input: "
            f"head={test_info['head']}, n={test_info['n']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


if __name__ == "__main__":
    test()
