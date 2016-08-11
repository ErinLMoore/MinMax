import sys
from src.Player import Player

#result a = min(b)
#result b = min(c)
#RETURN whichever one's bigger

class MinMax(object):

    def __init__(self, list_of_actions):
        self.list_of_actions= list_of_actions
        self.player = self.create_player()

    def minmax_decision(self, state):
        resultant_states = self._nextStepFromState(state)
        if len(resultant_states) == 0:
            return None
        else:
            poss_states = self.player.return_possible_states(state)
            utility_list = [self._min_value(a) for a in poss_states]
            return poss_states[utility_list.index(max(utility_list))]

    def _nextStepFromState(self, state):
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
        return Player(self.list_of_actions)

    def _terminal_test(self, state):
        raise NotImplementedError

    def _calculate_utility_value(self, state):
        raise NotImplementedError
