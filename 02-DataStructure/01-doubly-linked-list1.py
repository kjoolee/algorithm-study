"""
Doubly Linked List Implementation

    - head node가 있는 경우 (원형 이중 연결 리스트)
    - 공백 상태에서는 head node의 llink와 rlink가 head node를 가리킴
    - 삽입, 삭제가 O(1) 시간에 가능
"""

class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.llink = None
        self.rlink = None


class DoublyLinkedList:
    def __init__(self):
        self.head = DListNode()

        self.head.llink = self.head
        self.head.rlink = self.head


    def insert(self, before, data):
        newnode = DListNode(data)

        newnode.llink = before
        newnode.rlink = before.rlink
        before.rlink.llink = newnode
        before.rlink = newnode

        return newnode


    def delete(self, removed):
        if removed == self.head:
            return

        removed.llink.rlink = removed.rlink
        removed.rlink.llink = removed.llink


    def print_list(self):
        p = self.head.rlink

        while p != self.head:
            print(p.data, end=" ")
            p = p.rlink

        print()

if __name__ == '__main__':

    L = DoublyLinkedList()

    n1 = L.insert(L.head, 10)
    n2 = L.insert(n1, 20)
    n3 = L.insert(n2, 30)

    L.print_list()

    L.delete(n2)

    L.print_list()