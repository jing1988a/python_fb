class TrieNode:
    # children = dict()
    # isEnd = False    这是 java 的搞法  在python 里这就是static  每个class 都能access  很崩!!!!!!!!!
    def __init__(self):
        self.children=dict()
        self.isEnd=False

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    root=TrieNode()
    def addWord(self, word):
        # write your code here
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.isEnd=True


    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        cur=self.root
        l=len(word)
        return self.searchNode(cur , word , 0 , l)
    def searchNode(self , cur , word , idx , l):
        if idx==l:
            if cur.isEnd:
                return True
            else:
                return False
        if word[idx]=='.':
            for c in cur.children.values():
                if self.searchNode(c , word , idx+1 , l):
                    return True
            return False
        else:
            if word[idx] in cur.children:
                return self.searchNode(cur.children[word[idx]] , word , idx+1 , l)
            else:
                return False

test=WordDictionary()
test.addWord('a')
# test.addWord('a')
# test.search(".")
# test.search('a')
print(test.search('aaaaa'))


#
#
# Input
# addWord("a")
# addWord("a")
# search(".")
# search("a")
# search("aa")
# search("a")
# search(".a")
# search("a.")
# Output
# [true,true,true,true,true,true]
# Expected
# [true,true,false,true,false,false]