import unittest
import mock
from src.RootNode import RootNode


class test_MinMax(unittest.TestCase):

    def setUp(self):
        pass

    def test_rootNodeReturnOwnState(self):
        exampleVector = [1,0,0]
        testRootNode = RootNode(exampleVector)
        expected = exampleVector
        actual = testRootNode.getState()
        self.assertEqual(expected, actual)
