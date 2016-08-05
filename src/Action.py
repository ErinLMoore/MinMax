from src.State import State

class Action(object):

    def __init__(self, list_of_actions):
        self.list_of_actions = list_of_actions

    def create_resultant_states_or_terminal_values(self, state):
        raise NotImplementedError

    def calculate_terminal_value(self, state):
        raise NotImplementedError

    def return_resultant_states_or_terminal_values(self, state):
        return_value = self.create_resultant_states_or_terminal_values(state)
        return return_value
