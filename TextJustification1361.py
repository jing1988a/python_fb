class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        # write your code here
        ans=[]
        curLen=0
        candidate=[]
        for w in words:
            n=len(w)
            if n>maxWidth:
                return []
            if curLen==0:
                curLen=n
                candidate.append(w)
            else:
                if curLen+n+1<=maxWidth:
                    curLen+=n+1
                    candidate.append(w)
                else:
                    ans.append(self.myFormat(candidate , maxWidth))
                    candidate=[w]
                    curLen=n
        if candidate:
            ans.append(' '.join(candidate).ljust(maxWidth , ' '))
        return ans
    def myFormat(self , candidate , maxWidth):
        l=len(candidate)
        if l==1:
            return candidate[0].ljust(maxWidth , ' ')
        total=0
        space=l-1
        for c in candidate:
            total+=len(c)
        spaceNeed=(maxWidth-total)//(l-1)
        extra=(maxWidth-total)%(l-1)
        ans=[candidate[0]]
        for i in range(1 , l):
            ans.append(' '*spaceNeed)
            if extra:
                ans.append(' ')
                extra-=1
            ans.append(candidate[i])
        return ''.join(ans)