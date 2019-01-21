# Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.
#
# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
#
# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.
#
# Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.
#
# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
#
# Example:
#
# Given width = 3, height = 2, and food = [[1,2],[0,1]].
#
# Snake snake = new Snake(width, height, food);
#
# Initially the snake appears at position (0,0) and the food at (1,2).
#
# |S| | |
# | | |F|
#
# snake.move("R"); -> Returns 0
#
# | |S| |
# | | |F|
#
# snake.move("D"); -> Returns 0
#
# | | | |
# | |S|F|
#
# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
#
# | |F| |
# | |S|S|
#
# snake.move("U"); -> Returns 1
#
# | |F|S|
# | | |S|
#
# snake.move("L"); -> Returns 2 (Snake eats the second food)
#
# | |S|S|
# | | |S|
#
# snake.move("U"); -> Returns -1 (Game over because snake collides with border)

import collections

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """

        self.board=[[None for i in range(width)] for j in range(height)]
        self.board[0][0]='S'
        self.width=width
        self.height=height
        self.food=list(reversed(food))
        self.snake=collections.deque()
        self.snake.append([0 , 0])
        if self.food:
            f=self.food.pop()
            self.board[f[0]][f[1]]='F'
        self.foodEaten=0





    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """

        # print(self.board)
        # print(self.snake)
        newH=[]
        if direction=='U':
            newH=[self.snake[-1][0]-1 , self.snake[-1][1]]
        elif direction=='L':
            newH = [self.snake[-1][0], self.snake[-1][1]-1]
        elif direction == 'R':
            newH = [self.snake[-1][0], self.snake[-1][1] + 1]
        elif direction == 'D':
            newH = [self.snake[-1][0]+1, self.snake[-1][1]]


        if newH[0]<0 or newH[0]>=self.height or newH[1]<0 or newH[1]>=self.width or (self.board[newH[0]][newH[1]]=='S' and newH !=self.snake[0]):
            return -1

        if self.board[newH[0]][newH[1]]=='F':
            self.snake.append(newH)
            self.board[newH[0]][newH[1]] = 'S'
            if self.food:
                f = self.food.pop()
                self.board[f[0]][f[1]] = 'F'

            self.foodEaten+=1
            return self.foodEaten
        else:
            self.snake.append(newH)
            tail = self.snake.popleft()
            self.board[newH[0]][newH[1]] = 'S'
            self.board[tail[0]][tail[1]] = None

            return self.foodEaten

["SnakeGame","move","move","move","move","move","move","move","move","move","move","move","move"]
[[3,3,[[2,0],[0,0],[0,2],[2,2]]],["D"],["D"],["R"],["U"],["U"],["L"],["D"],["R"],["R"],["U"],["L"],["D"]]



test=SnakeGame(3,3,[[2,0],[0,0],[0,2],[2,2]])
test.move("D")
test.move("D")
test.move("R")
test.move("U")
test.move("U")
test.move("L")
test.move("D")
test.move("R")
test.move("R")
test.move("U")
test.move("L")
test.move("D")

# Output
# [null,0,1,1,1,1,2,2,2,2,3,3,-1]
#
# Expected
# [null,0,1,1,1,1,2,2,2,2,3,3,3]

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)