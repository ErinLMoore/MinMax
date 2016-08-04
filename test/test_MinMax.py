import unittest
import mock
from src.RootNode import RootNode
from numpy import *


class test_MinMax(unittest.TestCase):

    def setUp(self):
        pass

    def test_rootNodeReturnOwnState(self):
        exampleState = [1,0,0]
        testRootNode = RootNode(exampleState)
        expected = exampleState
        actual = testRootNode.getState()
        self.assertEqual(expected, actual)

    def fake_getState(self):
        return [1,0,0]

    def test_actionFunctionTakesInRootAndReturnsResultants(self):
        testRootNode = RootNode([])
        testRootNode.getState() = self.fake_getState()
        testAction = Action(testRootNode)
