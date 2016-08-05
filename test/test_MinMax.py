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

    def fake_return_terminal_values(self, state):
        if state.get_state() == 'd': return [State('e'), State('f')]
        else: return 1 if state.get_state() == 'e' else 0


    def fake_calculate_resultant_states_or_terminal_values(self, state):
        original_state = state.get_state()
        actions_list = [d[state] for d in self.list_of_actions if state in d]
        return_list = [State(new_state, original_state) for new_state in actions_list]
        return return_list

    def test_rootNodeReturnOwnState(self):
        testRootNode = State('a')
        expected = 'a'
        actual = (testRootNode.get_state())

        self.assertEqual(expected, actual)

    def test_rootNodeReturnOwnPrecipitatingAction(self):
        testRootNode = State('a', 'b')
        expected = 'b'
        actual = (testRootNode.get_precipitating_action())

        self.assertEqual(expected, actual)

    def test_rootNodeReturnOwnUtility(self):
        testRootNode = State('a', 'b', 'c')
        expected = 'c'
        actual = (testRootNode.get_utility())

        self.assertEqual(expected, actual)

    def test_create_terminal_value_raises_error(self):
        testAction = Action(self.test_action_list)
        self.assertRaises(NotImplementedError,testAction.calculate_terminal_value, 'a')

    def test_calculate_resultant_states_or_terminal_values(self):
        testAction = Action(self.test_action_list)
        self.assertRaises(NotImplementedError,testAction.return_resultant_states_or_terminal_values, 'a')



    def test_action_handles_terminal_states(self):
        testAction = Action(self.test_action_list)
        testRootNode = Mock()
        testRootNode.get_state.return_value = 'd'
        testAction.calculate_terminal_value = Mock(return_value=1)
        testAction.create_resultant_states_or_terminal_values = Mock(return_value=1)
        expected = 1
        actual = testAction.return_resultant_states_or_terminal_values(testRootNode)
        self.assertEqual(expected, actual)

    def test_minmax_given_terminal_node_returns_utility(self):
        fakeRootNode = State('d')

        testMinMax = MinMax(self.test_action_list)
        testMinMax.action = Mock()
        testMinMax.action.return_resultant_states_or_terminal_values.return_value = 1

        expected = 1
        actual = testMinMax.bestActionFromRootNode(fakeRootNode)
        self.assertEqual(expected, actual)

    def test_minmax_finds_max_of_two_terminal_states_given_root_node(self):
        fakeRootNode = State('d')

        testMinMax = MinMax(self.test_action_list)

        fakeAction = Mock()
        fakeAction.return_resultant_states_or_terminal_values = self.fake_return_terminal_values
        testMinMax.action = fakeAction

        expected = 'e'
        actual = testMinMax.bestActionFromRootNode(fakeRootNode).get_state()
        self.assertEqual(expected, actual)

    def test_minmax_finds_min_of_two_terminal_states_given_root_node(self):
        fakeRootNode = State('d')

        testMinMax = MinMax(self.test_action_list)
        testMinMax.toggle_turn()
        fakeAction = Mock()
        fakeAction.return_resultant_states_or_terminal_values = self.fake_return_terminal_values
        testMinMax.action = fakeAction

        expected = 'f'
        actual = testMinMax.bestActionFromRootNode(fakeRootNode).get_state()
        self.assertEqual(expected, actual)

    def test_max_min_turn_toggles(self):
        fakeRootNode = State('d')

        testMinMax = MinMax(self.test_action_list)

        fakeAction = Mock()
        fakeAction.return_resultant_states_or_terminal_values = self.fake_return_terminal_values
        testMinMax.action = fakeAction
        testMinMax.bestActionFromRootNode(fakeRootNode)

        expected = 'min'
        actual = testMinMax.turn
        self.assertEqual(expected, actual)
