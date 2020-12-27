# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findParentDepth(self, node, x, parentVal = None, parentDepth = 0):
    if node.val == x:
      return [parentVal, parentDepth]
    if node.left:
      p = self.findParentDepth(node.left, x, node.val, parentDepth + 1)
      if p is not None:
        return p
    if node.right:
      q = self.findParentDepth(node.right, x, node.val, parentDepth + 1)
      if q is not None:
        return q
    return None
        
  def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    if root is None:
      return False
    p1 = self.findParentDepth(root, x);
    p2 = self.findParentDepth(root, y);
    if p1 is None or p2 is None:
      return False
    return p1[0] != p2[0] and p1[1] == p2[1]
