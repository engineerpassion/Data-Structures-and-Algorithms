class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():

    def __init__(self):
        self.root = None
    
    def is_empty(self):
        empty = False
        if self.root is None:
            empty = True
        return empty
    
    def search(self, value, return_parent_also=False):
        parent = None
        node = None
        if not self.is_empty():
            temp_parent = temp = self.root
            while temp != None:
                if temp.value == value:
                    node = temp
                    break
                elif temp.value > value:
                    temp_parent = temp
                    temp = temp.left
                else:
                    temp_parent = temp
                    temp = temp.right
            parent = temp_parent
        if return_parent_also:
            return parent, node
        else:
            return node
    
    def add_in_sub_tree(self, node: TreeNode, value):
        if node is None:
            node = TreeNode(value)
        elif node.value > value:
            node.left = self.add_in_sub_tree(node.left, value)
        elif node.value < value:
            node.right = self.add_in_sub_tree(node.right, value)
        return node
    
    def get_max_value(self):
        max_value = None
        if not self.is_empty():
            temp = self.root
            while temp.right is not None:
                temp = temp.right
            max_value = temp.value
        return max_value
    
    def get_min_value(self):
        min_value = None
        if not self.is_empty():
            temp = self.root
            while temp.left is not None:
                temp = temp.left
            min_value = temp.value
        return min_value
    
    def floor(self, k, root=None, return_node=False):
        floor_value = None
        floor_node = None
        root = self.root if root is None else root
        if root is not None:
            temp = root
            while temp is not None:
                if temp.value > k:
                    temp = temp.left
                elif temp.value == k:
                    floor_value = k
                    floor_node = temp
                    break
                else:
                    floor_value = temp.value
                    floor_node = temp
                    temp = temp.right
        if return_node:
            return floor_node
        else:
            return floor_value
    
    def ceil(self, k, root=None, return_node=False):
        ceil_value = None
        ceil_node = None
        root = self.root if root is None else root
        if root is not None:
            temp = root
            while temp is not None:
                if temp.value < k:
                    temp = temp.right
                elif temp.value == k:
                    ceil_value = k
                    ceil_node = temp
                    break
                else:
                    ceil_value = temp.value
                    ceil_node = temp
                    temp = temp.left
        if return_node:
            return ceil_node
        else:
            return ceil_value
    
    def delete_min(self, root=None):
        root = self.root if root is None else root
        if root is not None:
            temp = temp_parent = root
            while temp.left is not None:
                temp_parent = temp
                temp = temp.left
            if temp == temp_parent:
                if temp.right is not None:
                    root = temp.right
                else:
                    # There is only one node (root) in the tree
                    root = None
                    temp = None
            else:
                temp_parent.left = temp.right
        return root
    
    def delete_max(self, root=None):
        root = self.root if root is not None else root
        if root is not None:
            temp = temp_parent = root
            while temp.right is not None:
                temp_parent = temp
                temp = temp.right
            if temp == temp_parent:
                if temp.right is not None:
                    root = temp.left
                    del temp
                else:
                    # There is only one node (root) in the tree
                    root = None
                    del temp
            else:
                temp_parent.right = temp.left
                del temp
        return
    
    def delete(self, value):
        if not self.is_empty():
            # Searching for the value in tree
            parent, node = self.search(value, return_parent_also=True)
            if node.left is None and node.right is None:
                # There are no children to the node
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
                del node
            elif node.left is None:
                # There is only right child sub-tree
                if parent.right == node:
                    parent.right = node.right
                elif parent.left == node:
                    parent.left = node.right
                del node
            elif node.right is None:
                # There is only left child sub-tree
                if parent.right == node:
                    parent.right = node.left
                elif parent.left == node:
                    parent.left = node.right
                del node
            else:
                # Both left and right child sub-trees are present
                successor_node = self.ceil(node.value, root=node.right, return_node=True)
                print("successor_node.value: {}".format(successor_node.value))
                # Swapping the value with successor node value
                node.value, successor_node.value = successor_node.value, node.value
                # Deleting the min node in right sub-tree
                node.right = self.delete_min(root=node.right)
        return
    
    def add(self, value):
        self.root = self.add_in_sub_tree(self.root, value)
        return
    
    def inorder_traversal(self, node: TreeNode, order: str):
        if node is not None:
            order = self.inorder_traversal(node.left, order)
            order += str(node.value) + " "
            order = self.inorder_traversal(node.right, order)
        return order
    
    def inorder(self):
        order = self.inorder_traversal(self.root, "")
        order = order[0:len(order) - 1]
        print(order)
        return order
    
    def preorder_traversal(self, node: TreeNode, order: str):
        if node is not None:
            order += str(node.value) + " "
            order = self.preorder_traversal(node.left, order)
            order = self.preorder_traversal(node.right, order)
        return order
    
    def preorder(self):
        order = self.preorder_traversal(self.root, "")
        order = order[0:len(order) - 1]
        print(order)
        return
    
    def postorder_traversal(self, node: TreeNode, order: str):
        if node is not None:
            order = self.postorder_traversal(node.left, order)
            order = self.postorder_traversal(node.right, order)
            order += str(node.value) + " "
        return order
    
    def postorder(self):
        order = self.postorder_traversal(self.root, "")
        order = order[0:len(order) - 1]
        print(order)
        return

def main():
    bst = BinarySearchTree()
    print("Created an empty Binary Search Tree!")
    print("Adding 1.")
    bst.add(1)
    print("Inorder looks as follows:")
    bst.inorder()
    print("Preorder looks as follows:")
    bst.preorder()
    print("Postorder looks as follows:")
    bst.postorder()
    print("Adding 4.")
    bst.add(4)
    print("Inorder looks as follows:")
    bst.inorder()
    print("Preorder looks as follows:")
    bst.preorder()
    print("Postorder looks as follows:")
    bst.postorder()
    print("Adding 2.")
    bst.add(2)
    print("Adding 5.")
    bst.add(5)
    print("Adding 3.")
    bst.add(3)
    print("Inorder looks as follows:")
    bst.inorder()
    print("Preorder looks as follows:")
    bst.preorder()
    print("Postorder looks as follows:")
    bst.postorder()
    print("Removing 3.")
    bst.delete(3)
    print("Inorder looks as follows:")
    bst.inorder()
    print("Preorder looks as follows:")
    bst.preorder()
    print("Postorder looks as follows:")
    bst.postorder()
    print("Removing 4.")
    bst.delete(4)
    print("Inorder looks as follows:")
    bst.inorder()
    print("Preorder looks as follows:")
    bst.preorder()
    print("Postorder looks as follows:")
    bst.postorder()
    print("Removing 1.")
    bst.delete(1)
    print("Inorder looks as follows:")
    bst.inorder()
    print("Preorder looks as follows:")
    bst.preorder()
    print("Postorder looks as follows:")
    bst.postorder()
    print("Max value in the tree is: {}".format(bst.get_max_value()))
    print("Min value in the tree is: {}".format(bst.get_min_value()))
    print("Floor of 4 in the tree is: {}".format(bst.floor(4)))
    print("Floor of 10 in the tree is: {}".format(bst.floor(10)))
    print("Ceil of 4 in the tree is: {}".format(bst.ceil(4)))
    print("Ceil of 0 in the tree is: {}".format(bst.ceil(0)))
    print("Deleting minimum value from tree!")
    bst.delete_min()
    print("Inorder looks as follows:")
    bst.inorder()
    print("Preorder looks as follows:")
    bst.preorder()
    print("Postorder looks as follows:")
    bst.postorder()
    print("Deleting maximum value from tree!")
    bst.delete_max()
    print("Inorder looks as follows:")
    bst.inorder()
    print("Preorder looks as follows:")
    bst.preorder()
    print("Postorder looks as follows:")
    bst.postorder()

"""
Uncomment the following line to run the file.
"""
#main()