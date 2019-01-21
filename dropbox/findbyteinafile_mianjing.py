import collections
class Findsubstr:
    def find(self , candidate , strs):
        l1=len(strs)
        l2=len(candidate)
        if l1<l2:
            return False
        for i in range(l1-l2+1):
            if candidate==strs[i:i+l2]:
                return True
        return False

    #compare char one by one
    def find2(self , candidate , strs):
        l1=len(strs)
        l2=len(candidate)
        if l1<l2:
            return False
        for i in range(l1-l2+1):
            j=0
            while j<l2:
                if candidate[j]!=strs[j+i]:
                    break
                j+=1
            if j==l2:
                return True
        return False
    #compare with rolling hash
    def find3(self , candidate , strs):
        l1=len(strs)
        l2=len(candidate)
        candidateHash=self.getHash(candidate)
        curHash=self.getHash(strs[:l2])
        if candidateHash==curHash:
            return True
        i=1
        while i <l1-l2+1:
            curHash=self.getNextHash(strs[i-1] , strs[i+l2-1], curHash)
            if curHash==candidateHash:
                return True
        return False
    def getHash(self , strs):
        res=0
        for c in strs:
            res+=ord(c)
        return res
    def getNextHash(self , charToRemove , charToAdd , curHash):
        return curHash-ord(charToRemove)+ord(charToAdd)

    #what if file is too big
    def searchInFile(self , fileLoc  , candidate):
        BufferSize=self.getBufferSize()
        FileSize=self.getFileSize(fileLoc)

        curIdx=0
        while curIdx<FileSize:
            curBuffer=self.readFile(fileLoc , curIdx , BufferSize)
            if self.find3(candidate ,curBuffer):
                return True
            curIdx=curIdx+curBuffer-len(candidate)+1
        return False

    #File太大让用stream读进来。这轮还可以感觉
    def searchInFileStream(self, fileLoc, candidate):
        candidateHash=self.getHash(candidate)

        with getFileStream(fileLoc) as fs:
            curHash=0
            curStr=collections.deque()
            for i in range(len(candidate)):
                if not fs.hasNext():
                    return False
                c=fs.getNext()
                curHash+=ord(c)
                curStr.append(c)
            if curHash==candidateHash:
                return True
            while fs.hasNext():
                c=fs.getNext()
                curHash=self.getNextHash(curStr.popleft() , c , curHash)
                curStr.append(c)
                if curHash==candidateHash:
                    return True
            return False
