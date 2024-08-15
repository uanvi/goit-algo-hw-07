class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def sum_of_values(root):
    if root is None:
        return 0
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)

# Test
root = Node(5)
insert(root, 3)
insert(root, 2)
insert(root, 4)
insert(root, 7)
insert(root, 6)
insert(root, 8)

# Знаходимо найбільше значення в дереві
max_node = max_value_node(root)
print("Найбільше значення у дереві:", max_node.val)

min_node = min_value_node(root)
print("Найменше значення у дереві:", min_node.val)

sum_values = sum_of_values(root)
print("Сума всіх значень у дереві:", sum_values)