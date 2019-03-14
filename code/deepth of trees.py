# 二叉树深度
# -*- coding:utf-8 -*-

# 树节点定义
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, Root):
        if Root is None:
            return 0
        A = [Root]
        depth = 0
        while A:
            B = []
            for node in A:
                if node.left is not None:
                    B.append(node.left)
                if node.right is not None:
                    B.append(node.right)
            A = B
            depth += 1
        return depth


