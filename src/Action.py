from src.State import State

class Action(object):
    #performs a function on a state to return list of resulting states
    #root node must be passed in as hashable

    def __init__(self, actionDict):
        self.action_dict = actionDict

    def lookupActions(self, root_node):
        return self.action_dict[root_node]

    def performActionOnRootState(self, root_node):
        raise NotImplementedError

    def return_states(self, root_node):
        tuple_of_actions = self.lookupActions(root_node)
        print(tuple_of_actions)
        resultant_states = self.performActionOnRootState(root_node, tuple_of_actions)
        created_states = [State(state, action) for state, action in resultant_states]
