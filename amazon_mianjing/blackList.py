class BlackList:
    def solve(self , strs ,  text):
        strs=list(strs)
        tire=self.generateTrie(text)
        l=len(strs)
        for i in range(l):
            if strs[i] in tire.root.children:
                if self.checkInTrie(strs , i , l , tire.root ):
                    return True
        return False

    def checkInTrie(self ,strs , i , l , root):
        if root.isEnd:
            return True
        if i==l:
            return False
        if strs[i] in root.children:
            return self.checkInTrie(strs , i+1 , l , root.children[strs[i]])
        return False
    def generateTrie(self ,text):
        trie=Trie()
        for t in text:
            trie.add(t)
        return trie

class Trie:
    def __init__(self ):
        self.root=TrieNode()
    def add(self , word):
        cur=self.root
        for w in word:
            if w not in cur.children:
                cur.children[w]=TrieNode()
            cur=cur.children[w]
        cur.isEnd=True
class TrieNode:

    def __init__(self , ):

        self.children=dict()
        self.isEnd=False


# strs='abcd'
# root=TrieNode()
# a=TrieNode('a')
# b=TrieNode('b')
# c=TrieNode('c')
# d=TrieNode('c')
# d.isEnd=True
# b.isEnd=True
# d.isEnd=True
# root.children['a']=a
# root.children['c']=c
# a.children['c']=d


test=BlackList()
print(test.solve('cccab' , [ 'cba' , 'eee' , 'aca']))
 #    abcd
 #
 #        root
 #
 #    c       a
 #                b
 #
 # b  a
 #       b