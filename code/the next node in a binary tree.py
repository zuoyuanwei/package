给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
例{8,6,10,5,7,9,11},5，输出6

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:			# 中序遍历，下一个节点为右子树的某一个节点			
            left1=pNode.right	
            while left1.left:	# 遍历右子树时仍按照左根右的顺序，因此先遍历右子树的左节点
                left1=left1.left
            return left1		# 直到返回最左边的节点
        # p=pNode
        while pNode.next:		# 判断当前节点是否为叶节点
            tmp=pNode.next
            if tmp.left==pNode:	# 如果当前节点是最左边的叶节点时
                return tmp
            pNode=tmp