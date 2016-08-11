import unittest
from mock import Mock

from src.Player import Player
from src.State import State
from src.MinMax import MinMax

class test_MinMax(unittest.TestCase):

    def setUp(self):
        MinMax.create_player = self.fake_create_player

        self.fake_player = Mock()
        self.fake_player.return_possible_states= self.fake_return_possible_states
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

        self.test_action_list = [
        {'a': self.fake_stateB, 'b': self.fake_stateD, 'c': self.fake_stateF},
        {'a': self.fake_stateC, 'b': self.fake_stateE, 'c': self.fake_stateG}
        ]

        self.minmax_to_test = MinMax(self.test_action_list)
        self.minmax_to_test._calculate_utility_value = self.fake_calculate_utility_value
        self.minmax_to_test._terminal_test = self.fake_terminal_test

    def fake_create_player(self):
        return self.fake_player

    def fake_return_it(self, val):
        return val

    def fake_calculate_utility_value(self, state):
        state_name = state.get_state()
        if state_name == 'd':
            return 1
        elif state_name in ['g','e']:
            return -1
        else: return 0

    def fake_return_possible_states(self, state):
        original_state = state.get_state()
        return_list = [d[original_state] for d in self.test_action_list if original_state in d]
        return return_list

    def fake_terminal_test(self, state):
        return state.get_state() in ['d', 'e', 'f', 'g']

    def test_state_raises_correct_error(self):
        testState= State()
        self.assertRaises(NotImplementedError,testState.get_state)

    def test_look_up_resultant_states_raises_correct_error(self):
        testPlayer = Player(self.test_action_list)
        self.assertRaises(NotImplementedError,testPlayer._look_up_possible_actions, 'a')

    def test_calculate_terminal_value_raises_correct_error(self):
        minmax_to_test= MinMax(self.test_action_list)
        self.assertRaises(NotImplementedError,minmax_to_test._calculate_terminal_value, 'a')

    def test_calculate_terminal_value_raises_correct_error(self):
        minmax_to_test= MinMax(self.test_action_list)
        self.assertRaises(NotImplementedError,minmax_to_test._terminal_test, 'a')

    def test_minmax_handles_terminal_states(self):
        minmax_to_test = MinMax(self.test_action_list)
        expected = None
        actual = minmax_to_test.minmax_decision(self.fake_stateG)

        self.assertEqual(expected, actual)

    def test_minmax_finds_max_of_two_terminal_states_given_root_node(self):
        expected = 0
        actual = self.minmax_to_test.minmax_decision(self.fake_stateC)

        self.assertEqual(expected, actual)

        expected = 1
        actual = self.minmax_to_test.minmax_decision(self.fake_stateB)

        self.assertEqual(expected, actual)

    def test_minmax_finds_max_with_walk_of_two_nodes(self):
        expected = -1
        actual = self.minmax_to_test.minmax_decision(self.fake_stateA)

        self.assertEqual(expected, actual)
