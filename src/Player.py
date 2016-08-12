from src.State import State

class Player(object):

    def _look_up_possible_actions(self, state):
        raise NotImplementedError

    def return_possible_states(self, state):
        return_value = self._look_up_resultant_states(state)
        return return_value
