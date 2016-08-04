import unittest
import mock
from src.RootNode import RootNode
from src.Action import Action
import numpy as np


class test_MinMax(unittest.TestCase):

    def setUp(self):
        pass


    def arrangeTestActionsDict(self):
        self.initial_state = np.array([[1],[0],[0]])
        self.win_state = np.array([[0],[1],[0]])
        self.lose_state = np.array([[0],[0],[1]])
        self.win_action = np.array([[0,1,0],[0,0,0],[0,0,0]])
        self.lose_action = np.array([[0,0,1],[0,0,0],[0,0,0]])
        return {Action.array_to_tuple(self.initial_state): [self.win_action, self.lose_action],
                Action.array_to_tuple(self.win_state): 1,
                Action.array_to_tuple(self.lose_state): 0}

    def test_rootNodeReturnOwnState(self):
        exampleState = [1,0,0]
        testRootNode = RootNode(exampleState)
        expected = exampleState
        actual = testRootNode.getState()
        self.assertEqual(expected, actual)

    def fake_getState(self):
        return self.initial_state

    def fake_resultantAction(self):
        pass

    @mock.patch('src.RootNode.RootNode.getState', side_effect=fake_getState)
    def test_actionFunctionLookupActions(self, mock_get_state):
        testRootNode = RootNode([])
        testdict = self.arrangeTestActionsDict()
        testAction = Action(testdict)
        expected = [self.win_action, self.lose_action]
        actual = testAction.lookupActions(testRootNode)
        self.assertEqual(expected, actual)
