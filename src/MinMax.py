from src.Action import Action

class MinMax(object):
    #has a player
    #gives you a single action from a single state
    # the minimax value of a terminal state is just its utility

    def __init__(self, list_of_actions):
        self.action = Action(list_of_actions)

    def bestActionFromRootNode(self, root_state):
        self.nextStepFromState(root_state)
        if root_state.get_utility() is not None:
            return None
        else:
            return None

    def nextStepFromState(self, state):
        return_value = self.action.return_resultant_states_or_terminal_values(state)
        if isinstance(return_value, int):
            state.utility = return_value
