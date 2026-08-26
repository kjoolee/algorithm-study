class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


    # --------------------------------
    # INSERT
    # --------------------------------
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)


    def _insert_recursive(self, node, key):

        # 빈 위치에 새로운 노드 삽입
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key)

        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)

        # 중복 key는 삽입하지 않음
        return node


    # --------------------------------
    # DELETE
    # --------------------------------
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)


    def _delete_recursive(self, node, key):

        # 삭제할 노드가 없는 경우
        if node is None:
            return None

        # 삭제할 key 탐색
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)

        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)

        # 삭제할 노드를 찾은 경우
        else:

            # Case 1: 왼쪽 자식이 없음
            if node.left is None:
                return node.right

            # Case 2: 오른쪽 자식이 없음
            if node.right is None:
                return node.left

            # Case 3: 자식이 두 개인 경우
            # 오른쪽 subtree에서 가장 작은 값(successor)을 찾음
            successor = self._find_min(node.right)

            # successor의 값을 현재 노드로 복사
            node.key = successor.key

            # successor 노드 삭제
            node.right = self._delete_recursive(
                node.right, successor.key
            )

        return node


    # --------------------------------
    # Minimum node
    # --------------------------------
    def _find_min(self, node):

        while node.left is not None:
            node = node.left

        return node


    # --------------------------------
    # Inorder Traversal
    # --------------------------------
    def inorder(self):
        self._inorder_recursive(self.root)
        print()


    def _inorder_recursive(self, node):

        if node is not None:
            self._inorder_recursive(node.left)
            print(node.key, end=" ")
            self._inorder_recursive(node.right)

if __name__ == "__main__":
    tree = BST()

    for key in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(key)

    tree.inorder()
    # 20 30 40 50 60 70 80


    tree.delete(20)     # 자식 없음
    tree.inorder()
    # 30 40 50 60 70 80


    tree.delete(30)     # 자식 하나
    tree.inorder()
    # 40 50 60 70 80


    tree.delete(50)     # 자식 둘
    tree.inorder()
    # 40 60 70 80                