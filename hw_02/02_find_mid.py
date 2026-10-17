class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode) -> ListNode:
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


def test():
    test_data = [
        {
            "head": [1, 2, 3, 4, 5],
            "answer": [3, 4, 5]
        },
        {
            "head": [1, 2],
            "answer": [2]
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
            "answer": [7, -1]
        },
        {
            "head": [2, 2, 3, 2],
            "answer": [3, 2]
        },
        {
            "head": [1, 2, 3],
            "answer": [2, 3]
        },
        {
            "head": [1, 2, 3, 4, 5, 6],
            "answer": [4, 5, 6]
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


def answer_on_question():
    ans = """
    Быстрый указатель делает два шага, а медленный - один.
    Когда быстрый достигает конца списка, медленный оказывается в середине.
    При чётной длине выбирается второй из двух средних узлов.
    Повторный обход не нужен: время - O(n), дополнительная память - O(1).
    """
    print(ans)

if __name__ == "__main__":
    test()
    answer_on_question()

