# Design an in-memory file system to simulate the following functions:
#
# ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.
#
# mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.
#
# addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.
#
# readContentFromFile: Given a file path, return its content in string format.
#
#
#
# Example:
#
# Input:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
#
# Output:
# [null,[],null,null,["a"],"hello"]
#
# Explanation:
# filesystem
#
#
# Note:
#
# You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
# You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
# You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.
#

class Node:

    def __init__(self ):
        self.name=None
        self.children=dict()
        self.isFile=False
        self.content=""
class FileSystem(object):

    def __init__(self):
        self.root=Node()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        # will ls alwasy to a valid path or it can be invalid path??
        p=path.split('/')

        cur=self.root
        for v in p:
            if not v:
                continue
            cur=cur.children[v]
        if cur.isFile:
            return [cur.name]
        else:
            return sorted(cur.children.keys())


    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        p=path.split('/')
        cur=self.root
        for v in p:
            if not v:
                continue
            if not v in cur.children:
                cur.children[v]=Node()
                cur.children[v].name=v
            cur=cur.children[v]


    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        p=filePath.split('/')
        cur=self.root
        for v in p:
            if not v:
                continue
            if not v in cur.children:
                cur.children[v] = Node()
                cur.children[v].name=v
            cur = cur.children[v]
        cur.content+=content
        cur.isFile=True

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        p = filePath.split('/')
        cur=self.root
        for v in p:
            if not v:
                continue
            if not v in cur.children:
                cur.children[v] = Node
            cur = cur.children[v]
        return cur.content
# ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
# [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]

test=FileSystem()
test.ls("/")
test.mkdir("/a/b/c")


# ["FileSystem","mkdir","ls","ls","mkdir","ls","ls","addContentToFile","ls","ls","ls"]
# [[],["/goowmfn"],["/goowmfn"],["/"],["/z"],["/"],["/"],["/goowmfn/c","shetopcy"],["/z"],["/goowmfn/c"],["/goowmfn"]]
# Output
# [null,null,[],["goowmfn"],null,["goowmfn","z"],["goowmfn","z"],null,[],[],["c"]]
# Expected
# [null,null,[],["goowmfn"],null,["goowmfn","z"],["goowmfn","z"],null,[],["c"],["c"]]
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)