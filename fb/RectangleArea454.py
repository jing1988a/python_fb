class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here

    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    # write your code here
    width=0
    height=0
    def __init__(self , a , b):
        self.width=a
        self.height=b
    def getArea(self):
        return self.width*self.height