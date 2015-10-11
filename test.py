__author__ = 'Jessie'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        print self.recuisiveCount(root, 1)

    def recuisiveCount(self, node, n):
        if node.left:
            print "left", node.val
            n = self.recuisiveCount(node.left, n + 1)

        if node.right:
            print "right", node.val
            n = self.recuisiveCount(node.right, n + 1)
        return n


if __name__=="__main__":

    tree_1 = TreeNode(1)
    tree_2 = TreeNode(2)
    tree_3 = TreeNode(3)
    tree_4 = TreeNode(4)
    tree_5 = TreeNode(5)
    tree_6 = TreeNode(6)

    tree_1.left = tree_2
    tree_1.right = tree_3
    tree_2.left = tree_4
    tree_2.right = tree_5
    tree_3.left = tree_6

    test = Solution()
    test.countNodes(tree_1)