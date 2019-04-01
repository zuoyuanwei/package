输入一棵二叉树，判断该二叉树是否是平衡二叉树。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        if abs(self.Depth(pRoot.left)-self.Depth(pRoot.right)) > 1:
            return False
        else:
            return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
        
    def Depth(self,pRoot):
        if not pRoot:
            return 0
        Left = self.Depth(pRoot.left)
        Right = self.Depth(pRoot.right)
        return max(Left, Right)+1
                    