import time
from bintrees import RBTree
from bintrees import AVLTree
from bintrees import BinaryTree


class BinaryTreeWrapper(BinaryTree):
    def __init__(self):
        super().__init__()

    def _depth(self, node):
        if node is None:
            return 0
        left_depth = self._depth(node.left)
        right_depth = self._depth(node.right)
        return max(left_depth, right_depth) + 1
    
    def _iterative_depth(self, node):
        max_depth = 0
        stack = [(node, 1)]  # 노드와 현재 깊이를 튜플로 스택에 저장
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth    

    def get_depth(self):
        if self._root is None:
            return 0
        return self._iterative_depth(self._root)
    
class AVLTreeWrapper(AVLTree):
    def __init__(self):
        super().__init__()

    def _depth(self, node):
        if node is None:
            return 0
        left_depth = self._depth(node.left)
        right_depth = self._depth(node.right)
        return max(left_depth, right_depth) + 1

    def get_depth(self):
        if self._root is None:
            return 0
        return self._depth(self._root)


class RBTreeWrapper(RBTree):
    def __init__(self):
        super().__init__()

    def _depth(self, node):
        if node is None:
            return 0
        left_depth = self._depth(node.left)
        right_depth = self._depth(node.right)
        return max(left_depth, right_depth) + 1

    def get_depth(self):
        if self._root is None:
            return 0
        return self._depth(self._root)
    
    def _get_node(self, key):
        node = self._root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def get_color(self, key):
        node = self._get_node(key)
        if node is None:
            raise KeyError("Key not found in the tree")
        return 'Red' if node.red else 'Black'    



if __name__ == '__main__' :

    
    
    bi_tree  = BinaryTreeWrapper()
    rb_tree  = RBTreeWrapper()
    avl_tree = AVLTreeWrapper()
    
    
    with open('E2KLex.txt', encoding='utf8') as f:
        start_time = time.time()
        for line in f:
            items = line.strip().split('\t')
            key, value = items[0:2]
            bi_tree.insert(key, value)
        end_time = time.time()
    print(f'Binary Tree: {end_time-start_time} seconds')
    
    with open('E2KLex.txt', encoding='utf8') as f:
        start_time = time.time()
        for line in f:
            items = line.strip().split('\t')
            key, value = items[0:2]
            avl_tree.insert(key, value)            
        end_time = time.time()
    print(f'AVL Tree: {end_time-start_time} seconds')

    with open('E2KLex.txt', encoding='utf8') as f:
        start_time = time.time()
        for line in f:
            items = line.strip().split('\t')
            key, value = items[0:2]
            rb_tree.insert(key, value)
        end_time = time.time()
    print(f'RB Tree: {end_time-start_time} seconds')

    hash = dict()
    with open('E2KLex.txt', encoding='utf8') as f:
        start_time = time.time()
        for line in f:
            items = line.strip().split('\t')
            key, value = items[0:2]
            hash[key] = value
        end_time = time.time()
    print(f'HASH: {end_time-start_time} seconds')

    ######### retrieve
    with open('E2KLex.txt', encoding='utf8') as f:
        start_time = time.time()
        for line in f:
            items = line.strip().split('\t')
            key = items[0]
            value = avl_tree.get(key)
        end_time = time.time()
    print(f'AVL Tree Retrieval: {end_time-start_time} seconds')

    with open('E2KLex.txt', encoding='utf8') as f:
        start_time = time.time()
        for line in f:
            items = line.strip().split('\t')
            key = items[0]
            value = rb_tree.get(key)
        end_time = time.time()
    print(f'RB Tree Retrieval: {end_time-start_time} seconds')

    with open('E2KLex.txt', encoding='utf8') as f:
        start_time = time.time()
        for line in f:
            items = line.strip().split('\t')
            key = items[0]
            value = hash.get(key)
        end_time = time.time()
    print(f'HASH Retrieval: {end_time-start_time} seconds')


    print(rb_tree.nlargest(10))
    print(rb_tree.max_item())
    