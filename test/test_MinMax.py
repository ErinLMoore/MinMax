import unittest
from mock import Mock

from src.Action import Action
from src.State import State
from src.MinMax import MinMax


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
        testRootNode = Mock()
        testRootNode.get_state.return_value = 'a'
        testAction = Action(self.test_action_list)
        test_state = testRootNode.get_state()

        expected = ['b', 'c']
        actual = testAction.lookupActions(test_state)

        self.assertEqual(expected, actual)

    def test_calculate_terminal_value_raises_error(self):
        testAction = Action(self.test_action_list)
        self.assertRaises(NotImplementedError,testAction.calculate_terminal_value, 'a')


    def test_actionCreatesAndReturnsProperResultantStates(self):
        testAction = Action(self.test_action_list)
        testRootNode = Mock()
        testRootNode.get_state.return_value = 'a'

        expected = [['b', 'a', None], ['c','a', None]]
        results = testAction.return_resultant_states_or_terminal_values(testRootNode)
        actual = [[s.get_state(),s.get_precipitating_action(),s.get_utility()] for s in results]
        self.assertEqual(expected, actual)

    def test_action_handles_terminal_states(self):
        testAction = Action(self.test_action_list)
        testRootNode = Mock()
        testRootNode.get_state.return_value = 'd'
        testAction.calculate_terminal_value = Mock(return_value=1)
        expected = 1
        actual = testAction.return_resultant_states_or_terminal_values(testRootNode)
        self.assertEqual(expected, actual)

    def test_minmax_given_terminal_node_returns_none(self):
        testRootNode = Mock()
        testRootNode.get_state.return_value = 'd'
        testMinMax = MinMax(self.test_action_list)
        testAction = Mock()
        testAction.return_resultant_states_or_terminal_values.return_value = 1

        expected = None
        actual = testMinMax.bestActionFromRootNode(testRootNode)
        self.assertEqual(expected, actual)

    def xtest_minmax_finds_max_of_two_terminal_states_given_root_node(self):
        testRootNode = Mock()
        testRootNode.get_state.return_value = 'd'
        testMinMax = MinMax(self.test_action_list)
        testAction = Mock()
        testAction.return_resultant_states_or_terminal_values.return_value = 1
