import unittest
import mock
from src.RootNode import RootNode
from src.Action import Action
import numpy as np


class test_MinMax(unittest.TestCase):

    def setUp(self):
        pass

    def array_to_tuple(self, array):
        return tuple([tuple(i) for i in tuple(array)])

    def arrangeTestActionsDict(self):
        initial_state = np.array([[1],[0],[0]])
        win_state = np.array([[0],[1],[0]])
        lose_state = np.array([[0],[0],[1]])
        winAction = np.array([[0,1,0],[0,0,0],[0,0,0]])
        loseAction = np.array([[0,0,1],[0,0,0],[0,0,0]])
        return {self.array_to_tuple(initial_state): [winAction, loseAction],
                self.array_to_tuple(win_state): 1,
                self.array_to_tuple(lose_state): 0}

    def test_rootNodeReturnOwnState(self):
        exampleState = [1,0,0]
        testRootNode = RootNode(exampleState)
        expected = exampleState
        actual = testRootNode.getState()
        self.assertEqual(expected, actual)

    def fake_getState(self):
        return [1,0,0]

    def fake_resultantAction(self):
        pass

    @mock.patch('src.RootNode.RootNode.getState', side_effect=fake_getState)
    def test_actionFunctionLookupActions(self, mock_get_state):
        testRootNode = RootNode([])
        testdict = self.arrangeTestActionsDict()
        testAction = Action(testdict)
        expected = [np.array([[0,1,0],[0,0,0],[0,0,0]]), np.array([[0,0,1],[0,0,0],[0,0,0]])]
        actual = testAction.lookupActions(testRootNode)
        self.assertEqual(expected, actual)
