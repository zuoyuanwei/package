# 广度优先遍历,使用队列实现，出队的顶点变成黑色，在队列里的是灰色，还没入队的是白色。
# a.首先选择一个顶点作为起始顶点，并将其染成灰色，其余顶点为白色。
# b.将起始顶点放入队列中。
# c.从队列首部选出一个顶点，并找出所有与之邻接的顶点，
# 将找到的邻接顶点放入队列尾部，将已访问过顶点涂成黑色，没访问过的顶点是白色。
# 如果顶点的颜色是灰色，表示已经发现并且放入了队列，如果顶点的颜色是白色，表示还没有发现
# d.按照同样的方法处理队列中的下一个顶点。
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue
from pythonds.graphs import Graph


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' +word[i+1:]
            if bucket in d:
                d[bucket].apppend(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.setColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


def traverse(y):
    x = y
    while x.getPred():
        print(x.getId)
        x = x.getPred
    print(x.getId())


traverse(g.getVertex('sage'))