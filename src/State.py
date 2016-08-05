class State(object):

    def __init__(self, state, utility= None):
        self.state = state
        self.utility = utility

    def get_state(self):
        return self.state

    def get_utility(self):
        return self.utility

    def set_utility(self, utility):
        self.utility = utility
