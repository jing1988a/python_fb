# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
#
# Notice
# The read function may be called multiple times.
#
#


"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""
import collections


class Solution:
    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def __init__(self):
        self.generalBuff = collections.deque()

    def read(self, buf, n):
        # Write your code here
        if n <= 0:
            raise Exception('invalid input')
        buff4 = [None for _ in range(4)]
        i = 0
        while i < n:
            while self.generalBuff:
                buf[i]=self.generalBuff.popleft()
                i += 1
                if i == n:
                    return i
            while i < n:
                length4 = Reader.read4(buff4)
                if length4 == 0:
                    # end of file
                    return i
                j=0
                while j<length4:
                    buf[i]=buff4[j]
                    i+=1
                    j+=1
                    if i==n:
                        while j<length4:
                            self.generalBuff.append(buff4[j])
                            j+=1
                        return i

class Reader:
    def read4(self):
        return 0
