import sys
from src.Player import Player

class MinMax(object):

    def __init__(self, list_of_actions):
        self.list_of_actions= list_of_actions
        self.turn = 'max'
        self.player = self.create_player()

    def minmax_decision(self, state):
        resultant_states = self._nextStepFromState(state)
        if len(resultant_states) == 0:
            return None
        else:
            return self._max_value(state)

    def _nextStepFromState(self, state):
        return_value = self.player.return_possible_states(state)
        return return_value

    def create_player(self):
        return Player(self.list_of_actions)

    def _max_value(self, state):
      v = -sys.maxsize
      if self._terminal_test(state):
          return self._calculate_utility_value(state)
      for a in self.player.return_possible_states(state):
          temp = self._min_value(a)
          if temp >  v:
              v = temp
      return v

    def _min_value(self, state):
      v = sys.maxsize
      if self._terminal_test(state):
          return self._calculate_utility_value(state)
      for a in self.player.return_possible_states(state):
          temp = self._max_value(a)
          if temp <  v:
              v = temp
      return v

    def _terminal_test(self, state):
        raise NotImplementedError

    def _calculate_utility_value(self, state):
        raise NotImplementedError
