# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(p.val==q.val and p.left==None and p.left==None and p.right==None and q.right==None):
            return True
        elif (p.val==q.val):
            if p.left==q.left:
                isSameTree(p.left,q.left)
            if p.right == q.right:
                isSameTree(p.right,q.right)
        else:
            return False
                
s = Solution()
print(s.isSameTree(TreeNode([1,2]),TreeNode([1,None,2])))
