""" sorted binary tree

         9
       /   \
      5     15
     / \     \   
    2   6     20
       / \     \
      7   8     30   


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Tree
root = Node(9)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(6)
root.left.right.right = Node(8)
root.left.right.left = Node(7)
root.right.right = Node(20)
root.right.right.left = Node(30)

###################################  Traversing tree methods  ###############################


# Recursive inorder
def rec_inorder(root):
    if root is None:
        return

    #first, recursively tunnel down to left
    rec_inorder(root.left)

    # If dead end print leaf node
    print(root.data, end=' ')

    rec_inorder(root.right)

# Recursive preorder - like inorder but returns value as soon as node is visited
def rec_peorder(root):
    if root is None:
        return

    # Return data on visit to node, rather than store on stack
    print(root.data, end=' ')

    # And recurse left then right, as before
    rec_peorder(root.left)
    rec_peorder(root.right)

# Recursive postorder - left child, right child then parent returned in that order
def rec_postorder(root):
    if root is None:
        return
    
    # Do path checking before returning data
    rec_postorder(root.left)
    rec_postorder(root.right)
    print(root.data, end=' ')



print('\ninorder')
rec_inorder(root)
print('\npreorder')
rec_peorder(root)
print('\npostorder')
rec_postorder(root)
