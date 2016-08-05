from src.State import State

class Action(object):

    def __init__(self, list_of_actions):
        self.list_of_actions = list_of_actions

    def lookupActions(self, state):
        return_list =  [d[state] for d in self.list_of_actions if state in d]
        return return_list

    def return_resultant_states_or_terminal_values(self, root_node):
        original_state = root_node.get_state()
        return_list = [State(new_state, original_state) for new_state in  self.lookupActions(original_state)]
        return return_list if len(return_list) > 1 else self.calculate_terminal_value(root_node)

    def calculate_terminal_value(self, state):
        raise NotImplementedError
