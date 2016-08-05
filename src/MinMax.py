from src.Action import Action

class MinMax(object):
    #has a player
    #gives you a single action from a single state
    # the minimax value of a terminal state is just its utility

    def __init__(self, list_of_actions):
        self.action = Action(list_of_actions)
        self.turn = 'max'

    def bestActionFromRootNode(self, root_state):
        resultant_states = self.nextStepFromState(root_state)
        if isinstance(resultant_states, int):
            return root_state.get_utility()
        else:
            for i in resultant_states:
                self.nextStepFromState(i)
            return self.min_or_max(resultant_states)

    def nextStepFromState(self, state):
        return_value = self.action.return_resultant_states_or_terminal_values(state)
        if isinstance(return_value, int):
            state.set_utility(return_value)
        self.toggle_turn()
        return return_value

    def min_or_max(self, list_of_states):
        utilities_list = [i.get_utility() for i in list_of_states]
        max_utility = max(utilities_list)
        return_value = [i for i in list_of_states if i.get_utility() == max(utilities_list)]
        return return_value[0]

    def toggle_turn(self):
        turn_dict = {'min':'max', 'max':'min'}
        self.turn = turn_dict[self.turn]
