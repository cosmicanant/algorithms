class Solution:
    
    def traverse(self, node, counter, arr):
      res = False
      if counter == len(arr) - 1:
        if node.val == arr[counter] and not(node.left) and not(node.right):
          return True
        else:
          return False
      if node.val == arr[counter]:
        if node.left:
          res = self.traverse(node.left, counter + 1, arr)
          if res:
            return res
        if node.right:
          res = self.traverse(node.right, counter + 1, arr)
        return res
      else:
        return False
          
        
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
      if len(arr) == 0:
        return False
      res = self.traverse(root, 0, arr)
      return res