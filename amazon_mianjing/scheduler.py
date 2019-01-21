class MethodProfilling:
    def solve(self , logs):
        result=collections.defaultdict(int)
        curTime=0
        methodsQueue=[]
        for l in logs:
            method , type  , timestamp=l
            if not methodsQueue:
                methodsQueue.append(method)

            else:
                if type=='start':
                    curMethod=methodsQueue[-1]
                    result[curMethod]+=timestamp-curTime
                    methodsQueue.append(method)

                else:
                    curMethod = methodsQueue.pop()
                    result[curMethod] += timestamp - curTime
            curTime = timestamp
        return result
