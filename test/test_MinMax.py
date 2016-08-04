import unittest
import mock
from src.RootNode import RootNode
from src.Action import Action
import numpy as np


class test_MinMax(unittest.TestCase):

    def setUp(self):
        self.initiate_game_state()

    def array_to_tuple(self, array):
        return tuple([tuple(i) for i in tuple(array)])

    def initiate_game_state(self):
        self.initial_state = np.array([[1],[0],[0]])
        self.win_state = np.array([[0],[1],[0]])
        self.lose_state = np.array([[0],[0],[1]])
        self.win_action = np.array([[0,1,0],[0,0,0],[0,0,0]])
        self.lose_action = np.array([[0,0,1],[0,0,0],[0,0,0]])

    def arrangeTestActionsDict(self):
        return {self.array_to_tuple(self.initial_state): [self.win_action, self.lose_action],
                self.array_to_tuple(self.win_state): 1,
                self.array_to_tuple(self.lose_state): 0}

    def test_rootNodeReturnOwnState(self):
        testRootNode = RootNode(self.initial_state)
        expected =  True
        actual = (testRootNode.get_state()==self.initial_state).all()

        self.assertEqual(expected, actual)


    def test_actionFunctionLookupActions(self):
        testRootNode = mock.Mock()
        testRootNode.get_state.return_value = self.initial_state
        testdict = self.arrangeTestActionsDict()
        testAction = Action(testdict)
        test_state = self.array_to_tuple(testRootNode.get_state())

        expected = [self.win_action, self.lose_action]
        actual = testAction.lookupActions(test_state)

        self.assertEqual(expected, actual)

    def test_performActionOnRootStateRaisesError(self):
        testRootNode = mock.Mock()
        testdict = self.arrangeTestActionsDict()
        testAction = Action(testdict)

        self.assertRaises(NotImplementedError,testAction.performActionOnRootState, testRootNode)

    def xtest_actionCreatesAndReturnsResultantStates(self):
        self.initiate_game_state()
        testdict = self.arrangeTestActionsDict()
        testRootNode = mock.Mock()
        testRootNode.get_state.return_value = self.initial_state
        testAction = Action(testdict)

        #need to create 2 mock states to compare against
        #actual results

        #write test for notimplementederror
