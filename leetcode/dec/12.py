# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
class Solution:
    def dfs(self, node, currDepth):
        ldepth = currDepth
        rdepth = currDepth
        l, r = node, node
        if node.left:
            l, ldepth = self.dfs(node.left, currDepth + 1)
        if node.right:
            r, rdepth = self.dfs(node.right, currDepth + 1)
        if ldepth == rdepth:
            return [node, ldepth]
        elif ldepth > rdepth:
            return [l, ldepth]
        else:
            return [r, rdepth]
            
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        n, k = self.dfs(root, 0)
        return n