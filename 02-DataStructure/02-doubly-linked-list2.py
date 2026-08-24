class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    # 리스트의 맨 뒤에 삽입
    def insert(self, data):
        new_node = Node(data)

        # 빈 리스트인 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # 기존 리스트의 맨 뒤에 삽입
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


    # data를 가진 노드 삭제
    def delete(self, data):
        current = self.head

        # 삭제할 노드 탐색
        while current is not None:
            if current.data == data:
                break
            current = current.next

        # 삭제할 노드가 없는 경우
        if current is None:
            return

        # 이전 노드와 연결
        if current.prev is not None:
            current.prev.next = current.next
        else:
            # 첫 번째 노드를 삭제하는 경우
            self.head = current.next

        # 다음 노드와 연결
        if current.next is not None:
            current.next.prev = current.prev
        else:
            # 마지막 노드를 삭제하는 경우
            self.tail = current.prev


    # 출력
    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()

if __name__ == '__main__':

    L = DoublyLinkedList()

    L.insert(10)
    L.insert(20)
    L.insert(30)
    L.insert(40)

    L.print_list()
    # 10 20 30 40

    L.delete(20)

    L.print_list()
    # 10 30 40