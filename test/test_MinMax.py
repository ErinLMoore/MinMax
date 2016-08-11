import unittest
from mock import Mock
from test.create_test_states import create_test_states

from src.Player import Player
from src.State import State
from src.MinMax import MinMax

class test_MinMax(unittest.TestCase):

    def setUp(self):
        MinMax.create_player = self.fake_create_player

        create_test_states(self)

        self.test_action_list = [
        {'a': self.fake_stateB},
        {'a': self.fake_stateC},
        {'b': self.fake_stateD, 'c': self.fake_stateF},
        {'b': self.fake_stateE, 'c': self.fake_stateG},
        {'d': self.fake_stateH, 'e': self.fake_stateJ, 'f': self.fake_stateL, 'g': self.fake_stateN},
        {'d': self.fake_stateI, 'e': self.fake_stateK, 'f': self.fake_stateM, 'g': self.fake_stateO}
        ]

        self.minmax_to_test = MinMax(self.test_action_list)
        self.minmax_to_test._calculate_utility_value = self.fake_calculate_utility_value
        self.minmax_to_test._terminal_test = self.fake_terminal_test

    def fake_create_player(self):
        self.fake_player = Mock()
        self.fake_player.return_possible_states= self.fake_return_possible_states
        return self.fake_player

    def fake_calculate_utility_value(self, state):
        state_name = state.get_state()
        if state_name in ['i', 'n']:
            return 1
        elif state_name in ['h', 'k','l', 'm', 'o']:
            return -1
        else: return 0

    def fake_return_possible_states(self, state):
        original_state = state.get_state()
        return_list = [d[original_state] for d in self.test_action_list if original_state in d]
        return return_list

    def fake_terminal_test(self, state):
        return state.get_state() in ['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

    ###TESTS BEGIN###
    def test_state_raises_correct_error(self):
        testState = State()
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
        expected = None
        actual = self.minmax_to_test.minmax_decision(self.fake_stateO)

        self.assertEqual(expected, actual)

    def test_minmax_finds_max_of_two_terminal_states_given_one_node(self):
        expected = 0
        actual = self.minmax_to_test.minmax_decision(self.fake_stateE)

        self.assertEqual(expected, actual)

        expected = 1
        actual = self.minmax_to_test._max_value(self.fake_stateD)

        self.assertEqual(expected, actual)

    def test_minmax_finds_max_with_walk_of_two_nodes(self):
        expected = -1
        actual = self.minmax_to_test._max_value(self.fake_stateB)

        self.assertEqual(expected, actual)

    def test_minmax_finds_max_with_walk_of_three_nodes(self):
        expected = 0
        actual = self.minmax_to_test._max_value(self.fake_stateA)

        self.assertEqual(expected, actual)

    def test_minmax_return_best_action_from_node(self):
        expected = 'b'
        actual = self.minmax_to_test.minmax_decision(self.fake_stateA).get_state()

        self.assertEqual(expected, actual)
