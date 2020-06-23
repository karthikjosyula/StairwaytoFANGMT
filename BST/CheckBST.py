#Recursive
INT_MAX = 4294967296
INT_MIN = -4294967296
# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
    return (isBSTUtil(node, INT_MIN, INT_MAX))

# Retusn true if the given tree is a BST and its values
# >= min and <= max
def isBSTUtil(node, mini, maxi):
    # An empty tree is BST
    if node is None:
        return True
    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))

#Another approach
def isBST(root, l=None, r=None):
    # Base condition
    if (root == None):
        return True

    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if (l != None and root.data <= l.data):
        return False

    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if (r != None and root.data >= r.data):
        return False

    # check recursively for every node.
    return isBST(root.left, l, root) and \
           isBST(root.right, root, r)

