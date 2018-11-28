# /*
# 	 * Implement a function to return top rated movies in the network of movies
# 	 * reachable from the current movie eg: A(Rating 1.2) / \ B(2.4) C(3.6) \ /
# 	 * D(4.8) In the above example edges represent similarity and the number is
# 	 * rating. getMovieRecommendations(A,2) should return C and D (sorting order
# 	 * doesn't matter so it can also return D and C)
# 	 * getMovieRecommendations(A,4) should return A, B, C, D (it can also return
# 	 * these in any order eg: B,C,D,A) getMovieRecommendations(A,1) should
# 	 * return D. Note distance from A to D doesn't matter, return the highest
# 	 * rated.
# 	 *
# 	 * @param movie
# 	 *
# 	 * @param numTopRatedSimilarMovies number of movies we want to return
# 	 *
# 	 * @return List of top rated similar movies
# 	 */
import heapq


class Problem:
    def getMovieRecommendations(self, movie, k):
        hq = []
        self.recur(movie, k, hq)
        ans = []
        while hq:
            ans.append(hq.pop()[1])
        return ans

    def recur(self, node, k, hq):
        if not node:
            return
        heapq.heappush(hq, (node.rating, node.name))
        if len(hq) > k:
            heapq.heappop(hq)
        self.recur(node.left, k, hq)
        self.recur(node.right, k, hq)


class Node:
    def __init__(self, v=None, rating=None):
        self.name = v
        self.rating = rating
        self.left = None
        self.right = None


A = Node('A', 1.2)
B = Node('B', 2.4)
C = Node('C', 3.6)
D = Node('D', 4.8)
B.right=D
A.left=B
A.right=C
test = Problem()

print(test.getMovieRecommendations(A, 2))


# easy to think of a brute force way to traversing the whole tree, store node and rate in a array then
# sort the array by decending order and get the top K move name.
# but this way stores additiona movie info we do not need and sort also include
# moveis that we do no care. which is a waste of time and space. And ususally when we want top K of something
# heap will helps. which is the case in this question. a triky part of this question is that
# using a mean heap or max heap. originally I was thinking of max heap since it want
# top K highest rating but actually we need min heap since we need to track the smallest element
# in the heap and pop it when there are larger ones get pushed into.

