import unittest
import mock
from src.RootNode import RootNode
from src.Action import Action
from src.State import State
import numpy as np


class test_MinMax(unittest.TestCase):

    def setUp(self):
        self.initiate_game_state()

    def fake_return_it(self, val):
        return val

    def fake_performActionOnRootState(self, root_node, actions):
        return [[self.win_state, self.win_action], [self.lose_state, self.lose_action]]
        #return [[action, action.dot(root_node)] for action in actions]

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
        testRootNode = State(self.initial_state)
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
        args = [testRootNode, []]
        self.assertRaises(NotImplementedError,testAction.performActionOnRootState, testRootNode)


    def test_actionCreatesAndReturnsProperResultantStates(self):
        testdict = self.arrangeTestActionsDict()

        testAction = Action(testdict)

        testAction.performActionOnRootState = mock.Mock(return_value = \
        self.fake_performActionOnRootState(self.initial_state,
        testAction.lookupActions(self.array_to_tuple(self.initial_state))))


        expectedarray = [[self.win_state, self.win_action, 1], [self.lose_state, self.lose_action, 0]]
        results = testAction.return_states(self.array_to_tuple(self.initial_state))

        actualarray= [[i.get_state(), i.get_precipitating_action(), i.get_utility()] for i in results]
        print (actualarray[0][0])
        self.assertTrue(np.array_equal(expectedarray[0][0],actualarray[0][0]))
