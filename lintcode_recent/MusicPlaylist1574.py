# 1574. Music Playlist
# Ming likes to listen to music on his mobile phone while traveling by train. He has a n song on his mobile phone. He can listen to the p song on the whole train, so he wants to generate a playlist to produce a p song. The rules for this playlist are:
# (1) Each song must be played at least once
# (2) In the middle of two songs, there are at least m other songs.
# Xiao Ming wants to know how many different playlists can be produced. Since the result is large, the output result is the remainder of the 1000000007.
#
# Example
# Give n = 2, m = 0, p = 3,return 6。
#
# Explanation:
# There are 2 songs in total, which are recorded as A and B.
# No other songs are needed between the two songs.
# There are 6 programs in AAB, ABA, BAA, BBA, BAB and ABB.
# Give n = 1, m = 1, p = 3,return 0。
#
# Explanation:
# There is only one AAA scheme, but there are at least one other song
# in the middle of the same song, so there is no scheme that meets the requirements.
#
#

class Solution:
    """
    @param n: the number of on his mobile phone
    @param m: in the middle of two songs, there are at least m other songs
    @param p: the number of songs he can listen to
    @return: the number of playlists
    """
    def getAns(self, n, m, p):
        # Write your code here
        if m>=n:
            return 0
        dp=[[0 for _ in range(n+1)] for _ in range(p+1)]
        dp[0][0]=1
        for i in range(1 , p+1):
            for j in range(1 , n+1):
                dp[i][j]=dp[i-1][j-1]*(n-j+1)
                dp[i][j]+=dp[i-1][j]*max(0  , j-m)
        return dp[p][n]%1000000007