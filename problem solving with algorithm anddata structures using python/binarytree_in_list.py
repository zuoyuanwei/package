# 用列表实现树结构。
# 三个位置分别对应根节点，左节点，右节点。
def BinaryTree(r):
    return [r, [], []]
# 节点插入左子树，先判断原左子树是否有值，如果有值，将该值作为插入节点的左子节点。
def inserLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], [])
    return root
def getRootVal(root):
    return root[0]
def setRootVal(root, newVal):
    root[0] = newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]