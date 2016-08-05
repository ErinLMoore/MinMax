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


    def xtest_actionCreatesAndReturnsProperResultantStates(self):
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
