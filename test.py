import unittest
from unittest import result  #import unittest

# __import__("findsum.py")
from Summing import findsum    #     import exact function from folder

class TestSumList(unittest.TestCase):         #write function inside test class
    def test0(self):
        data=[2,35,7]
        result=findsum(data)
        self.assertEqual(result,44)
    def test1(self):
        data=[3.5,5.8,9]
        result=findsum(data)
        self.assertEqual(result,18.3)




if __name__ == '__main__':  #entry point for calling function
    unittest.main()
    # runner=TestSumList()
    # runner.test1()
    # singletest.addTes//t(MyTestSuite('test_false'))
