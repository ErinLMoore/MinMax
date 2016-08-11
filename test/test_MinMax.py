import unittest
from mock import Mock

from src.Player import Player
from src.State import State
from src.MinMax import MinMax


class test_MinMax(unittest.TestCase):

    def setUp(self):
        MinMax.create_player = self.fake_create_player

        self.test_action_list = [
        {'a':'b', 'b':'d', 'c':'f'},
        {'a':'c', 'b':'e', 'c':'g'}
        ]

        self.fake_player1 = Mock()
        self.fake_player1.return_possible_states= self.fake_return_possible_states
        self.fake_player2 = Mock()
        self.fake_player1.return_possible_states = self.fake_return_possible_states
        self.fake_stateA = Mock()
        self.fake_stateA.get_state.return_value = 'a'
        self.fake_stateB = Mock()
        self.fake_stateB.get_state.return_value = 'b'
        self.fake_stateC = Mock()
        self.fake_stateC.get_state.return_value = 'c'
        self.fake_stateD = Mock()
        self.fake_stateD.get_state.return_value = 'd'
        self.fake_stateE = Mock()
        self.fake_stateE.get_state.return_value = 'e'
        self.fake_stateF = Mock()
        self.fake_stateF.get_state.return_value = 'f'
        self.fake_stateG = Mock()
        self.fake_stateG.get_state.return_value = 'g'

        testMinMax = MinMax(self.test_action_list)
        testMinMax._calculate_terminal_value = self.fake_return_terminal_values
        testMinMax._min_value = self.fake_min
        testMinMax._max_value = self.fake_max
        testMinMax._terminal_test = self.fake_terminal_test

    def fake_create_player(self):
        return self.fake_player1

    def fake_return_it(self, val):
        return val

    def fake_return_terminal_values(self, state):
        if state in ['d', 'g']:
            return 1
        else: return 0

    def fake_min(self, state):
        utilities_list = [i.get_utility() for i in list_of_states]
        desired_utility = max(utilities_list) if self.turn == 'max' else min(utilities_list)
        return_value = [i for i in list_of_states if i.get_utility() == desired_utility]
        self._toggle_turn()
        return return_value[0]

    def fake_max(self, state):
        pass

    def fake_return_possible_states(self, state):
        original_state = state.get_state()
        actions_list = [d[state] for d in self.test_action_list if state in d]
        return_list = [State(new_state, original_state) for new_state in actions_list]
        return return_list

    def fake_terminal_test(self, state):
        return state in ['d', 'e', 'f', 'g']

    def test_state_raises_correct_error(self):
        testState= State()
        self.assertRaises(NotImplementedError,testState.get_state)

    def test_look_up_resultant_states_raises_correct_error(self):
        testPlayer = Player(self.test_action_list)
        self.assertRaises(NotImplementedError,testPlayer._look_up_possible_actions, 'a')

    def test_calculate_terminal_value_raises_correct_error(self):
        testMinMax= MinMax(self.test_action_list)
        self.assertRaises(NotImplementedError,testMinMax._calculate_terminal_value, 'a')

    def test_calculate_terminal_value_raises_correct_error(self):
        testMinMax= MinMax(self.test_action_list)
        self.assertRaises(NotImplementedError,testMinMax._terminal_test, 'a')

    def test_calculate_min_value_raises_correct_error(self):
        testMinMax= MinMax(self.test_action_list)
        self.assertRaises(NotImplementedError,testMinMax._min_value, 'a')

    def test_calculate_max_value_raises_correct_error(self):
        testMinMax= MinMax(self.test_action_list)
        self.assertRaises(NotImplementedError,testMinMax._max_value, 'a')

    def test_minmax_handles_terminal_states(self):

        testMinMax = MinMax(self.test_action_list)
        expected = None
        actual = testMinMax.minmax_decision(self.fake_stateG)
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
        testMinMax = MinMax(self.test_action_list)

        fakeAction = Mock()
        fakeAction.return_resultant_states_or_terminal_values = self.fake_return_terminal_values
        testMinMax.action = fakeAction
        testMinMax.bestActionFromRootNode(fakeRootNode)

        expected = 'min'
        actual = testMinMax.turn
        self.assertEqual(expected, actual)
