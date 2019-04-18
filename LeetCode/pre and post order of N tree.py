N叉树前序和后序遍历：
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :
前序遍历：[1,3,5,6,2,4]
返回其后序遍历: [5,6,3,2,4,1].
两种函数添加数值的顺序区别

前序遍历：
 """
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.result = []
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        self.result.append(root.val)
        for i in root.children:
            self.preorder(i)
        return self.result
		
后序遍历：
 """
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.result = []
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        for i in root.children:
            self.postorder(i)
        self.result.append(root.val)
        return self.result
    