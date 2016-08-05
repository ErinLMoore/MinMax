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
                print (i.get_utility())
            return self.min_or_max(resultant_states)

    def nextStepFromState(self, state):
        return_value = self.action.return_resultant_states_or_terminal_values(state)
        if isinstance(return_value, int):
            state.set_utility(return_value)
        return return_value

    def min_or_max(self, list_of_states):
        return_value = -1000
        thing_to_return = None
        for i in list_of_states:
            if i.get_utility() > return_value:
                return_value = i.get_utility()
                thing_to_return = i
        return thing_to_return
