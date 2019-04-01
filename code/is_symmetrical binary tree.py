请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def is_same(Left,Right):
            if not Left and not Right:
                return True
            if (Left and Right) and Left.val == Right.val:
                return is_same(Left.left, Right.right) and is_same(Left.right, Right.left)
            return False
        if not pRoot:
            return True
        if pRoot.left and not pRoot.right:
            return False
        if pRoot.right and not pRoot.left:
            return False
        return is_same(pRoot.left, pRoot.right)