输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
Tips：二叉搜索树的某一个节点比它左子树中任一个节点的值都大，比它右子树中任一个节点的值都小。
转化成双向链表即原树中指向左子树的指针变为链表中指向前一个节点的指针，原树中指向右子树的指针变为链表中指向后一个节点的指针。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left

        # 连接根与左子树最大结点
        if left:
            while(left.right):
                left=left.right
            pRootOfTree.left,left.right=left,pRootOfTree

        # 处理右子树
        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right
        
        # 连接根与右子树最小结点
        if right:
            while(right.left):
                right=right.left
            pRootOfTree.right,right.left=right,pRootOfTree
             
        while(pRootOfTree.left):
            pRootOfTree=pRootOfTree.left
        return pRootOfTree
