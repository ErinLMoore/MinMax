import unittest
from mock import Mock

from src.Player import Player
from src.State import State
from src.MinMax import MinMax


class test_MinMax(unittest.TestCase):

    def setUp(self):
        self.test_action_list = [
        {'a':'b', 'b':'d', 'c':'f'},
        {'a':'c', 'b':'e', 'c':'g'}
        ]
        fake_player1 = Mock()
        fake_player1.return_possible_states= self.fake_return_possible_states
        fake_player2 = Mock()
        fake_player1.return_possible_states = self.fake_return_possible_states
        fake_stateA = Mock()
        fake_stateA.get_state.return_value = 'a'
        fake_stateB = Mock()
        fake_stateB.get_state.return_value = 'b'
        fake_stateC = Mock()
        fake_stateC.get_state.return_value = 'c'
        fake_stateD = Mock()
        fake_stateD.get_state.return_value = 'd'
        fake_stateE = Mock()
        fake_stateE.get_state.return_value = 'e'
        fake_stateF = Mock()
        fake_stateF.get_state.return_value = 'f'
        fake_stateG = Mock()
        fake_stateG.get_state.return_value = 'g'

    def fake_return_it(self, val):
        return val

    def fake_return_terminal_values(self, state):
        if state.get_state() == 'd': return [State('e'), State('f')]
        else: return 1 if state.get_state() == 'e' else 0

    def fake_return_possible_states(self, state):
        original_state = state.get_state()
        actions_list = [d[state] for d in self.list_of_actions if state in d]
        return_list = [State(new_state, original_state) for new_state in actions_list]
        return return_list

    def test_state_raises_correct_error(self):
        testState= State()
        self.assertRaises(NotImplementedError,testState.get_state)

    def test_look_up_resultant_states(self):
        testPlayer = Player(self.test_action_list)
        self.assertRaises(NotImplementedError,testPlayer._look_up_possible_actions, 'a')

    def test_calculate_terminal_value(self):
        testMinMax= MinMax(self.test_action_list)
        self.assertRaises(NotImplementedError,testMinMax._calculate_terminal_value, 'a')

    def xtest_action_handles_terminal_states(self):
        testAction = Action(self.test_action_list)
        testRootNode = Mock()
        testRootNode.get_state.return_value = 'd'
        testAction._calculate_terminal_value = Mock(return_value=1)
        testAction._create_resultant_states_or_terminal_values = Mock(return_value=1)
        expected = 1
        actual = testAction.return_resultant_states_or_terminal_values(testRootNode)
        self.assertEqual(expected, actual)

    def xtest_minmax_given_terminal_node_returns_itself(self):
        fakeRootNode = State('d')

        testMinMax = MinMax(self.test_action_list)
        testMinMax.action = Mock()
        testMinMax.action.return_resultant_states_or_terminal_values.return_value = 1

        expected = 1
        actual = testMinMax.bestActionFromRootNode(fakeRootNode)
        self.assertEqual(expected, actual)

    def xtest_minmax_finds_max_of_two_terminal_states_given_root_node(self):
        fakeRootNode = State('d')

        testMinMax = MinMax(self.test_action_list)

        fakeAction = Mock()
        fakeAction.return_resultant_states_or_terminal_values = self.fake_return_terminal_values
        testMinMax.action = fakeAction

        expected = 1
        actual = testMinMax.bestActionFromRootNode(fakeRootNode)

    def xtest_minmax_finds_min_of_two_terminal_states_given_root_node(self):
        fakeRootNode = State('d')

        testMinMax = MinMax(self.test_action_list)
        testMinMax._toggle_turn()
        fakeAction = Mock()
        fakeAction.return_resultant_states_or_terminal_values = self.fake_return_terminal_values
        testMinMax.action = fakeAction

        expected = 0
        actual = testMinMax.bestActionFromRootNode(fakeRootNode)

    def xtest_max_min_turn_toggles(self):
        fakeRootNode = State('d')

        testMinMax = MinMax(self.test_action_list)

        fakeAction = Mock()
        fakeAction.return_resultant_states_or_terminal_values = self.fake_return_terminal_values
        testMinMax.action = fakeAction
        testMinMax.bestActionFromRootNode(fakeRootNode)

        expected = 'min'
        actual = testMinMax.turn
        self.assertEqual(expected, actual)
