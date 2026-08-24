"""
Doubly Linked List Implementation

    - head node가 없는 경우 

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    # 리스트의 맨 앞에 삽입
    def insert(self, data):
        pass

    # 리스트의 맨 뒤에 삽입
    def insert_last(self, data):
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

    # target_data를 가진 노드 뒤에 data를 가진 노드 삽입
    def insert_after(self, target_data, data):
        pass

    # 리스트의 맨 앞 노드 삭제
    def delete_first(self):
        pass

    # 리스트의 맨 뒤 노드 삭제
    def delete_last(self):
        pass

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


    # data 값을 가진 노드 검색
    # 찾으면 해당 노드를 반환, 없으면 None 반환
    def search(self, data):
        pass

    # head부터 tail까지 순서대로 출력
    def print_forward(self): 
        pass

    # tail부터 head까지 순서대로 출력
    def print_backward(self):
        pass
    

if __name__ == '__main__':

    # --------------------------------
    # Test
    # --------------------------------

    L = DoublyLinkedList()

    # 삽입 테스트
    L.insert_first(20)
    L.insert_first(10)
    L.insert_last(30)
    L.insert_last(40)

    print("Forward:")
    L.print_forward()
    # 예상 결과: 10 20 30 40

    print("Backward:")
    L.print_backward()
    # 예상 결과: 40 30 20 10


    # 중간 삽입 테스트
    L.insert_after(20, 25)

    print("After insert:")
    L.print_forward()
    # 예상 결과: 10 20 25 30 40


    # 삭제 테스트
    L.delete_first()
    L.delete_last()
    L.delete(25)

    print("After delete:")
    L.print_forward()
    # 예상 결과: 20 30


    # 탐색 테스트
    node = L.search(30)

    if node is not None:
        print("Found:", node.data)
    else:
        print("Not found")

    # 예상 결과: Found: 30