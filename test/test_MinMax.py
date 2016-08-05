import unittest
import mock

from src.Action import Action
from src.State import State


class test_MinMax(unittest.TestCase):

    def setUp(self):
        self.test_action_list = [
        {'a':'b', 'b':'d', 'c':'f'},
        {'a':'c', 'b':'e', 'c':'g'}
        ]

    def fake_return_it(self, val):
        return val

    def arrangeTestActionsDict(self):
        return {self.array_to_tuple(self.initial_state): [self.win_action, self.lose_action],
                self.array_to_tuple(self.win_state): 1,
                self.array_to_tuple(self.lose_state): 0}

    def test_rootNodeReturnOwnState(self):
        testRootNode = State(['a'])
        expected = ['a']
        actual = (testRootNode.get_state())

        self.assertEqual(expected, actual)


    def test_actionFunctionLookup(self):
        testRootNode = mock.Mock()
        testRootNode.get_state.return_value = 'a'
        testAction = Action(self.test_action_list)
        test_state = testRootNode.get_state()

        expected = ['b', 'c']
        actual = testAction.lookupActions(test_state)

        self.assertEqual(expected, actual)

    def xtest_performActionOnRootStateRaisesError(self):
        testRootNode = mock.Mock()
        testdict = self.arrangeTestActionsDict()
        testAction = Action(testdict)
        args = [testRootNode, []]
        self.assertRaises(NotImplementedError,testAction.performActionOnRootState, testRootNode)


    def test_actionCreatesAndReturnsProperResultantStates(self):
        testAction = Action(self.test_action_list)
        testRootNode = mock.Mock()
        testRootNode.get_state.return_value = 'a'

        expected = [['b', 'a', None], ['c','a', None]]
        results = testAction.return_states('a')
        actual = [[s.get_state(),s.get_precipitating_action(),s.get_utility()] for s in results]
        self.assertEqual(expected, actual)
