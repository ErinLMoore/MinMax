from src.Player import Player

class MinMax(object):

    def __init__(self, list_of_actions):
        self.list_of_actions= list_of_actions
        self.turn = 'max'
        self.player = self.create_player()

    def minmax_decision(self, state):
        #return action
        resultant_states = self._nextStepFromState(state)
        if len(resultant_states) == 0:
            return None
        else:
            for i in resultant_states:
                self._nextStepFromState(i)
            return self._min_or_max(resultant_states).get_utility()

    def _nextStepFromState(self, state):
        return_value = self.player.return_possible_states(state)
        return return_value

    def _toggle_turn(self):
        turn_dict = {'min':'max', 'max':'min'}
        self.turn = turn_dict[self.turn]

    def create_player(self):
        return Player(self.list_of_actions)

    def _max_value(self, state):
        raise NotImplementedError

    def _min_value(self, state):
        raise NotImplementedError

    def _terminal_test(self, state):
        raise NotImplementedError

    def _calculate_terminal_value(self, state):
        raise NotImplementedError
