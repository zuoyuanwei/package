从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        A = [pRoot]
        B = []
        while A:
            C = []
            for nodes in A:
                C.append(nodes.val)
            B.append(C)
            for i in range(len(A)):
                node = A.pop(0)
                if node.left:
                    A.append(node.left)
                if node.right:
                    A.append(node.right)
        return B
        