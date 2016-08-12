import sys
from src.Player import Player

class MinMax(object):

    def __init__(self):
        self.player = self.create_player()

    def minmax_decision(self, state):
        resultant_states = self._find_possible_states_from_state(state)
        if len(resultant_states) == 0:
            return None
        else:
            utility_list = [self._min_value(a) for a in resultant_states]
            return resultant_states[utility_list.index(max(utility_list))]

    def _find_possible_states_from_state(self, state):
        return_value = self.player.return_possible_states(state)
        return return_value

    def _max_value(self, state):
      if self._terminal_test(state):
          return self._calculate_utility_value(state)

      current_max_value = -sys.maxsize
      for action in self.player.return_possible_states(state):
          utility_of_action = self._min_value(action)
          if utility_of_action  >  current_max_value:
              current_max_value = utility_of_action
      return current_max_value

    def _min_value(self, state):
      if self._terminal_test(state):
          return self._calculate_utility_value(state)

      current_min_value = sys.maxsize
      for action in self.player.return_possible_states(state):
          utility_of_action  = self._max_value(action)
          if utility_of_action  <  current_min_value:
              current_min_value = utility_of_action
      return current_min_value

    def create_player(self):
        return Player()

    def _terminal_test(self, state):
        raise NotImplementedError

    def _calculate_utility_value(self, state):
        raise NotImplementedError
