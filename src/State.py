class State(object):
    #RESULT(s, a): The transition model, which defines the result of a move.
    #terminal test
    #utility of a state based on states under it
    def __init__(self, state, precipitating_action=None, utility= None):
        self.state = state
        self.precipitating_action = precipitating_action
        self.utility = utility

    def get_state(self):
        return self.state

    def get_precipitating_action(self):
        return self.precipitating_action

    def get_utility(self):
        return self.utility
