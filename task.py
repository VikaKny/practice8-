class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, data):
        current = self.root

        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            # Якщо є обидва нащадки
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete(node.right, min_node.data)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def toString(self):
        elements = []

        def traverse(node):
            if node is not None:
                traverse(node.left)
                elements.append(node.data)
                traverse(node.right)

        traverse(self.root)
        return elements

    def get_min(self):
        if self.root is None:
            return None

        return self._find_min(self.root).data

    def get_max(self):
        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right

        return current.data

    def count(self):
        def count_nodes(node):
            if node is None:
                return 0

            return 1 + count_nodes(node.left) + count_nodes(node.right)

        return count_nodes(self.root)


tree = BinaryTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(20)

print("Всі елементи дерева:", tree.toString())
print("Пошук числа 7:", tree.search(7))
print("Пошук числа 25:", tree.search(25))
print("Найменший елемент:", tree.get_min())
print("Найбільший елемент:", tree.get_max())
print("Кількість елементів:", tree.count())

tree.delete(5)

print("Дерево після видалення 5:", tree.toString())
print("Кількість після видалення:", tree.count())
