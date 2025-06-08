class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def dfs_non_recursive(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.value)  # Process the current node

        for child in reversed(node.children):
            stack.append(child)

# Example usage:
if __name__ == "__main__":
    # Creating a sample tree
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)
    child4 = TreeNode(5)
    child5 = TreeNode(6)

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child3)
    child1.add_child(child4)
    child2.add_child(child5)

    # Perform DFS traversal
    dfs_non_recursive(root)
