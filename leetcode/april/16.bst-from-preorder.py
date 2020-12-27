# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getNode(self, val):
        return TreeNode(val)

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = new TreeNode(preorder[0])
        stack = [root]
        for i in range(1, len(preorder)):
            currVal = preorder[i]
            node = self.getNode(currVal)
            parent = stack[-1]
            if currVal < parentVal:
                parent.left = node
                stack.append(currVal)
            else:
                while len(stack) > 1:
                    p = stack[-2]
                    if currVal > p.val:
                        stack.pop()
                    else:
                        break
                parent = stack.pop()
                parent.right = node
                stack.push(node)
        return root
