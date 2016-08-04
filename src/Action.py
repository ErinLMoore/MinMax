import src.State

class Action(object):
    #performs a function on a state to return list of resulting states

    def __init__(self, actionDict):
        self.action_dict = actionDict

    def lookupActions(self, rootNode):
        return self.action_dict[rootNode]

    def performActionOnRootState(self, rootNode):
        raise NotImplementedError
