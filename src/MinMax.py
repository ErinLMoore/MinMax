from src.Action import Action

class MinMax(object):

    def __init__(self, list_of_actions):
        self.action = Action(list_of_actions)
        self.turn = 'max'

    def bestActionFromRootNode(self, root_state):
        resultant_states = self._nextStepFromState(root_state)
        if isinstance(resultant_states, int):
            return root_state.get_utility()
        else:
            for i in resultant_states:
                self._nextStepFromState(i)
            return self._min_or_max(resultant_states)

    def _nextStepFromState(self, state):
        return_value = self.action.return_resultant_states_or_terminal_values(state)
        if isinstance(return_value, int):
            state.set_utility(return_value)
        return return_value

    def _min_or_max(self, list_of_states):
        utilities_list = [i.get_utility() for i in list_of_states]
        desired_utility = max(utilities_list) if self.turn == 'max' else min(utilities_list)
        return_value = [i for i in list_of_states if i.get_utility() == desired_utility]
        self._toggle_turn()
        return return_value[0]

    def _toggle_turn(self):
        turn_dict = {'min':'max', 'max':'min'}
        self.turn = turn_dict[self.turn]
