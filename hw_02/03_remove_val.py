class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head: ListNode, target: int) -> ListNode:
    dummy = ListNode()
    dummy.next = head 
    prev = dummy
    curr = head
    while curr is not None and curr.val != target:
        prev = curr
        curr = curr.next

    if curr is not None:
        prev.next = curr.next
    return dummy.next


def test():
    test_data = [
        {
            "head": [1, 2, 3, 4, 5],
            "target": 1,
            "answer": [2, 3, 4, 5]
        },
        {
            "head": [1, 2, 3, 4, 5],
            "target": 3,
            "answer": [1, 2, 4, 5]
        },
        {
            "head": [1, 2, 3],
            "target": 3,
            "answer": [1, 2]
        },
        {
            "head": [1],
            "target": 1,
            "answer": []
        },
        {
            "head": [],
            "target": 1,
            "answer": []
        },
        {
            "head": [1],
            "target": 2,
            "answer": [1]
        },
        {
            "head": [1, 2, 3],
            "target": 7,
            "answer": [1, 2, 3]
        },
        {
            "head": [-3, 0, 7, -1],
            "target": 0,
            "answer": [-3, 7, -1]
        },
        {
            "head": [2, 2, 3, 2],
            "target": 2,
            "answer": [2, 3, 2]
        },
        {
            "head": [1, 2, 2, 3],
            "target": 2,
            "answer": [1, 2, 3]
        },
    ]
    for test_info in test_data:
        
        head = None
        for val in test_info["head"][::-1]:
            head = ListNode(val, head)

        res_head = solution(head, test_info["target"])
        result = []

        while res_head is not None and len(result) <= len(test_info["head"]):
            result.append(res_head.val)
            res_head = res_head.next

        err_str = (
            f"\nTest failed for input: "
            f"head={test_info['head']}, target={test_info['target']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str


def answer_on_question():
    ans = """
    Перед головой создаём вспомогательный узел dummy, а prev указывает на него
    При удалении головы команда prev.next = curr.next меняет dummy.next
    на следующий узел, который становится новой головой.
    При удалении внутреннего узла та же команда связывает предыдущий узел
    со следующим, исключая найденный узел из цепочки.
    Если удаляем хвост, prev.next становится None.
    Если список пуст или значение не найдено, список не меняется.
    Возвращаем dummy.next - актуальную голову списка.
    """
    print(ans)

if __name__ == "__main__":
    test()
    answer_on_question()

