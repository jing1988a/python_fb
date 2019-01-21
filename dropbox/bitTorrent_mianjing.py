# 1. 给一堆Chunk和一个file size,问给定的一堆Chunk能不能组成complete file.
# Chunk就是一个左开右闭的区间, 如[0, 4)表示这个chunk包含0, 1, 2, 3这4个byte. 给定的size是这个文件大小.
# boolean isCompleteFile(List<Chunk> chunks, int size)
# 例如:.
# chunks = [[0, 1), [1, 3), [3, 4)]  size = 4   => 结果是true
# chunks = [[0, 1), [1, 3), [3, 4)]  size = 5   => 结果是false
# chunks = [[0, 1), [2, 3), [3, 4)]  size = 4   => 结果是false.1point3acres缃�
# .2. 实现一个ChunkManager class, 实现一个函数, isCompleteForNow(Chunk chunk), 每call一次这个函数,就会把chunk更新到这个类中,并判断当前类中已经有的list of chunk可不可以组成一个complete file..1point3acres缃�
# 例如:
# ChunkManager chunkManager = new ChunkManager(4);
# chunkManager.isCompleteForNow([0, 2)); -> false
# chunkManager.isCompleteForNow([2, 3)); -> true http://www.1point3acres.com/bbs/thread-194080-1-1.html
#
# 类似insert interval 要求多次插入，如何优化，用segmentation tree 超时写完

class ChunkManager:
    def isCompleteForNow(self, intervals, size):
        # assume chunks are sorted by start?
        if size <= 0:
            return True
        if len(intervals == 0):
            return False
        intervals.sort(lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if i[0] > end:
                return False
            else:
                end = max(end, i[1])
        return end == size


class ChunkManager:
    def __init__(self, size):
        self.size = size
        self.BST = BST()

    def isCompleteForNow(self, interval):
        # assume chunks are sorted by start?
        self.BST.insert(interval)
        if self.BST.root.start == 0 and self.BST.root.end == self.size:
            return True
        else:
            return False


class BST:
    def __init__(self):
        self.root = None

    def insert(self, interval):

        if not self.root:
            self.root = Node(interval[0], interval[1])
        else:
            if self.root.start > interval[1]:
                self.left = self.insert(self.root.left, interval)
            if self.root.end < interval[1]:
                self.right = self.insert(self.root.right, interval)
            else:
                self.root.start = min(self.root.start, interval[0])
                self.root.end = min(self.root.end, interval[1])
                self.mergeDown()

    def insert(self, node, interval):
        if not node:
            node = Node(interval[0], interval[1])
        else:
            if node.start > interval[1]:
                node.left = node.insert(node.left, interval)
            if node.end < interval[1]:
                node.right = node.insert(node.right, interval)
            else:
                node.start = min(node.start, interval[0])
                node.end = min(node.end, interval[1])
                self.mergeDown()
        return node


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None



这道题的最优解不应该是bitset吗， 想不明白为啥用tree
  static class ChunkManager {
        private int size;
        private BitSet set = new BitSet();
        public ChunkManager(int size) {
            this.size = size;
            set.set(0, size);
        }
        public boolean isCompleteForNow(Chunk chunk) {
            insert(chunk);
            return set.isEmpty();
        }
        private void insert(Chunk chunk) {. 1point3acres
            set.clear(chunk.start, chunk.end);
        }
    }