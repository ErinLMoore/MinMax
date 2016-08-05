from src.State import State

class Action(object):
    #performs a function on a state to return list of resulting states
    #root node must be passed in as hashable

    def __init__(self, list_of_actions):
        self.list_of_actions = list_of_actions

    def lookupActions(self, root_node):
        return_list =  [d[root_node] for d in self.list_of_actions]
        return return_list


    def return_states(self, root_node):
        tuple_of_actions = self.lookupActions(root_node)
        resultant_states = self.performActionOnRootState(root_node, tuple_of_actions)
        created_states = [State(state, action) for state, action in resultant_states]
        return created_states
