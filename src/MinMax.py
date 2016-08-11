from src.Player import Player

class MinMax(object):

    def __init__(self, list_of_actions):
        self.list_of_actions= list_of_actions
        self.turn = 'max'
        self.player = self.create_player()

    def bestActionFromRootNode(self, state):
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

    def _min_or_max(self, list_of_states):
        utilities_list = [i.get_utility() for i in list_of_states]
        desired_utility = max(utilities_list) if self.turn == 'max' else min(utilities_list)
        return_value = [i for i in list_of_states if i.get_utility() == desired_utility]
        self._toggle_turn()
        return return_value[0]

    def _calculate_terminal_value(self, state):
        raise NotImplementedError

    def _toggle_turn(self):
        turn_dict = {'min':'max', 'max':'min'}
        self.turn = turn_dict[self.turn]

    def create_player(self):
        return Player(self.list_of_actions)
