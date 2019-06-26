# 使用节点定义树结构，更符合面向对象的编程范例。
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if not self.leftChild:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if not self.rightChild:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # 二叉树的3种遍历方法。
    def preorder(tree):
        if tree:
            print(tree.getRootVal())
            preorder(tree.getLeftChild())
            preorder(tree.getRightChild())

    def posorder(tree):
        if tree:
            posorder(tree.getLeftChild())
            posorder(tree.getRightChild())
            print(tree.getRootVal())

    def inorder(tree):
        if tree:
            inorder(tree.getLeftChild())
            print(tree.getRootVal())
            inorder(tree.getRightChild())





r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
