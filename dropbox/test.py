import time
import unittest
from .DesignHitCounter361_mianjing import HitCounter
from .soda_mianjing import Buysoda


class TestSoda(unittest.TestCase):
    def setUp(self):
        self.buysoda=Buysoda()
    def testCase1(self):
        self.assertEqual(self.buysoda.solve([1 , 2 , 6] , 10) , [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1, 2, 2], [1, 1, 1, 1, 2, 2, 2], [1, 1, 1, 1, 6], [1, 1, 2, 2, 2, 2], [1, 1, 2, 6], [2, 2, 2, 2, 2], [2, 2, 6]])

# class TestCounterClass(unittest.TestCase):
#     def setUp(self):
#         self.counter = HitCounter()
#
#     def testCase1(self):
#         time.time = unittest.mock.MagicMock(return_value=1)
#         self.assertEqual(self.counter.hit(), None)
#         self.assertEqual(self.counter.queue[1], [1, 1])
#         time.time = unittest.mock.MagicMock(return_value=2)
#         self.assertEqual(self.counter.hit(), None)
#         time.time = unittest.mock.MagicMock(return_value=300)
#         self.assertEqual(self.counter.getHits(), 2)
#         time.time = unittest.mock.MagicMock(return_value=301)
#         self.assertEqual(self.counter.getHits(), 1)
#
#     def testCase2(self):
#         time.time = unittest.mock.MagicMock(return_value=1)
#         self.assertEqual(self.counter.getHits(), 0)


if __name__ == '__main__':
    unittest.main()
