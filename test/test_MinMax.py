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
        {self.stateA: self.stateB},
        {self.stateA: self.stateC},
        {self.stateB: self.stateD, self.stateC: self.stateF},
        {self.stateB: self.stateE, self.stateC: self.stateG},
        {self.stateD: self.stateH, self.stateE: self.stateJ, self.stateF: self.stateL, self.stateG: self.stateN},
        {self.stateD: self.stateI, self.stateE: self.stateK, self.stateF: self.stateM, self.stateG: self.stateO}
        ]

        self.minmax_to_test = MinMax()
        self.minmax_to_test._calculate_utility_value = self.fake_calculate_utility_value
        self.minmax_to_test._terminal_test = self.fake_terminal_test

    def fake_create_player(self):
        self.fake_player = Mock()
        self.fake_player.return_possible_states= self.fake_return_possible_states
        return self.fake_player

    def fake_calculate_utility_value(self, state):
        state_name = state
        if state_name in [self.stateI, self.stateN]:
            return 1
        elif state_name in [self.stateH, self.stateK, self.stateL, self.stateM, self.stateN]:
            return -1
        else: return 0

    def fake_alternate_calculate_utility_value(self, state):
        state_name = state
        if state_name in [self.stateK, self.stateL]:
            return 4
        elif state_name in [self.stateI, self.stateM,self.stateN]:
            return -2
        elif state_name in [self.stateH, self.stateJ]:
            return  3
        else: return 5

    def fake_return_possible_states(self, state):
        original_state = state
        return_list = [d[original_state] for d in self.test_action_list if original_state in d]
        return return_list

    def fake_terminal_test(self, state):
        return state in [self.stateH, self.stateI, self.stateJ, self.stateK, self.stateL, self.stateM, self.stateN, self.stateO]

    ###TESTS BEGIN###
    def test_state_raises_correct_error(self):
        testState = State()
        self.assertRaises(NotImplementedError,testState.get_state)

    def test_look_up_resultant_states_raises_correct_error(self):
        testPlayer = Player()
        self.assertRaises(NotImplementedError,testPlayer._look_up_possible_actions, self.stateA)

    def test_calculate_terminal_value_raises_correct_error(self):
        minmax_to_test= MinMax()
        self.assertRaises(NotImplementedError,minmax_to_test._calculate_terminal_value, self.stateA)

    def test_calculate_terminal_value_raises_correct_error(self):
        minmax_to_test= MinMax()
        self.assertRaises(NotImplementedError,minmax_to_test._terminal_test, self.stateA)

    def test_minmax_handles_terminal_states(self):
        expected = None
        actual = self.minmax_to_test.minmax_decision(self.stateO)

        self.assertEqual(expected, actual)

    def test_minmax_finds_max_of_two_terminal_states_given_one_node(self):
        expected = 0
        actual = self.minmax_to_test._max_value(self.stateE)

        self.assertEqual(expected, actual)

        expected = 1
        actual = self.minmax_to_test._max_value(self.stateD)

        self.assertEqual(expected, actual)

    def test_minmax_finds_min_of_two_terminal_states_given_one_node(self):
        expected = -1
        actual = self.minmax_to_test._min_value(self.stateD)

        self.assertEqual(expected, actual)

        expected = -1
        actual = self.minmax_to_test._min_value(self.stateE)

        self.assertEqual(expected, actual)

    def test_minmax_finds_maxmin_with_walk_of_two_nodes(self):
        expected = -1
        actual = self.minmax_to_test._max_value(self.stateB)

        self.assertEqual(expected, actual)

    def test_minmax_finds_maxmin_with_walk_of_three_nodes(self):
        expected = 0
        actual = self.minmax_to_test._max_value(self.stateA)

        self.assertEqual(expected, actual)

    def test_minmax_return_best_action_from_node(self):
        expected = self.stateB
        actual = self.minmax_to_test.minmax_decision(self.stateA)

        self.assertEqual(expected, actual)

    def test_minmax_return_best_action_from_node_alternate(self):
        self.minmax_to_test._calculate_utility_value = self.fake_alternate_calculate_utility_value
        expected = self.stateC
        actual = self.minmax_to_test.minmax_decision(self.stateA)

        self.assertEqual(expected, actual)
