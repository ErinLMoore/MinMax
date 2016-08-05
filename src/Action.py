from src.State import State

class Action(object):
    #performs a function on a state to return list of resulting states
    #root node must be passed in as hashable

    def __init__(self, list_of_actions):
        self.list_of_actions = list_of_actions

    def lookupActions(self, state):
        return_list =  [d[state] for d in self.list_of_actions]
        return return_list


    def return_states(self, root_node):
        original_state = root_node.get_state()
        return_list = [State(new_state, original_state) for new_state in  self.lookupActions(original_state)]
        return return_list

    def calculate_terminal_value(self, state):
        raise NotImplementedError
