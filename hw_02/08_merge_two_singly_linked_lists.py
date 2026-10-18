class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    curr = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    while list1 is not None:
        curr.next = list1
        list1 = list1.next
        curr = curr.next

    while list2 is not None:
        curr.next = list2
        list2 = list2.next
        curr = curr.next

    return dummy.next 

def test():
    test_data = [
        {
            "list1": [3, 6, 8],
            "list2": [4, 7, 9, 11],
            "answer": [3, 4, 6, 7, 8, 9, 11]
        },
        {
            "list1": [],
            "list2": [],
            "answer": []
        },
        {
            "list1": [],
            "list2": [1, 2],
            "answer": [1, 2]
        },
        {
            "list1": [1, 2],
            "list2": [],
            "answer": [1, 2]
        },
        {
            "list1": [1],
            "list2": [2],
            "answer": [1, 2]
        },
        {
            "list1": [2],
            "list2": [1],
            "answer": [1, 2]
        },
        {
            "list1": [1, 2],
            "list2": [3, 4],
            "answer": [1, 2, 3, 4]
        },
        {
            "list1": [3, 4],
            "list2": [1, 2],
            "answer": [1, 2, 3, 4]
        },
        {
            "list1": [1, 2, 2],
            "list2": [1, 2, 3],
            "answer": [1, 1, 2, 2, 2, 3]
        },
        {
            "list1": [-5, -1, 0],
            "list2": [-3, 0, 4],
            "answer": [-5, -3, -1, 0, 0, 4]
        },
    ]
    for test_info in test_data:
        list1 = None
        list2 = None
        nodes = set()
        for val in test_info["list1"][::-1]:
            list1 = ListNode(val, list1)
            nodes.add(list1)
        for val in test_info["list2"][::-1]:
            list2 = ListNode(val, list2)
            nodes.add(list2)

        res_head = solution(list1, list2)
        result = []
        result_nodes = set()
        while res_head is not None:
            assert res_head not in result_nodes, "В результате появился цикл"
            result_nodes.add(res_head)
            result.append(res_head.val)
            res_head = res_head.next

        err_str = (
            f"\nTest failed for input: "
            f"list1={test_info['list1']}, list2={test_info['list2']}\n"
            f"Expected: {test_info['answer']}, but got: {result}"
        )
        assert result == test_info["answer"], err_str
        assert result_nodes == nodes, "Результат должен содержать все исходные узлы"


def answer_on_question():
    ans = """
    Каждый из n + m узлов обрабатывается один раз, поэтому время - O(n + m).
    Меняем ссылки между существующими узлами, не копируя их.
    Используем только указатели и один вспомогательный узел dummy,
    поэтому дополнительная память - O(1).
    """
    print(ans)


if __name__ == "__main__":
    test()
    answer_on_question()
