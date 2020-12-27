class Solution:
  def search(self, node, k, arr = []):
    if node.left:
      res = self.search(node.left, k, arr)
      if res is not None:
        return res
    arr.append(node.val)
    if(len(arr) == k):
      return node.val
    if(node.right):
      res = self.search(node.right, k, arr)
      if res is not None:
        return res
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    return self.search(root, k, [])

"""
class Solution:
  def kthSmallest(self, root, k):
    stack = []
    while True:
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()
      k -= 1
      if not k:
        return root.val
      root = root.right
"""