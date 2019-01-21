class caculate:

    def solve(self , vals):
        newVals=self.reformat(vals)
        return self.realsolve(newVals)
    def realsolve(self  , newVs):

        s=[]
        op=[]
        l=len(newVs)
        cur=0
        i=0
        if newVs[0]=='-':
            s.append(0)
            op.append('-')
            i+=1
        while i<l:
            if isinstance(newVs[i] , int) :
                s.append(newVs[i])
                i+=1
            elif newVs[i] in ['-' , '+']:
                op.append(newVs[i])
                i+=1
            elif newVs[i] in ['*', '/']:
                a=s.pop()
                cal=newVs[i]
                i+=1
                b=newVs[i]
                if newVs[i]=='(':
                    j=i+1
                    count = 1
                    while count!=0:
                        # out of rance exception if invalid input
                        if newVs[j]=='(':
                            count+=1
                        elif newVs[j]==')':
                            count-=1
                        if count==0:
                            break
                        j+=1
                    b=self.solve(newVs[i+1:j])
                    i=j
                if cal=='*':
                    s.append(a*b)
                elif cal=='/':
                    s.append(a/b)
                i+=1
            elif newVs[i]=='(':
                j = i + 1
                count = 1
                while count != 0:
                    # out of rance exception if invalid input
                    if newVs[j] == '(':
                        count += 1
                    elif newVs[j] == ')':
                        count -= 1

                    if count == 0:
                        break
                    j += 1

                s.append(self.solve(newVs[i + 1:j]))
                i = j+1

        s.reverse()
        op.reverse()
        while op:
            a=s.pop()
            b=s.pop()
            o=op.pop()
            if o=='+':
                s.append(a+b)
            else:
                s.append(a-b)
        return s[-1]
    def reformat(self , v):
        ans=[]
        l=len(v)
        i=0
        cur=0

        while i<l:
            if v[i] in ['+' , '-' , '*' , '/' , ')' ]:
                if i-1>=0 and v[i-1]==')':
                    ans.append(v[i])
                else:
                    ans.append(cur)
                    ans.append(v[i])
                    cur=0
            elif v[i] == '(':
                ans.append(v[i])
            else:
                cur=cur*10+int(v[i])
            i+=1

        if v[-1]!=')':
            ans.append(cur)

        return ans










#
# 12
# [ '(' , '-' , 4 , '+' , 12 , ')' ,'/' , 2 , '*' , 3 , '+'  , '('  , 12 , '+' , 1, ')']
test=caculate()
print(test.reformat('(-4+12)/2*3+(12+1)'))
print(test.solve('(-4+12)/2*3+(12+1)'))
# print(test.reformat('(-4+12)/2*3+(12+1)'))
# print(test.solve('(-4+12)/2*3+(12+1)'))

