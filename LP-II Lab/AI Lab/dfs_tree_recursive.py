class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def dfs_recursive(node):
    if node is None:
        return

    print(node.value)  # Process the current node

    for child in node.children:
        dfs_recursive(child)

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
    dfs_recursive(root)
    
    
 
 #    1
 #   / \
 #  2   3
 # /\   /
 # 4 5 6
 
  
   
