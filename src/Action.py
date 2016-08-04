import src.ResultantState

class Action(object):
    #returns the set of legal moves in a stat(e

    def __init__(self, actionDict):
        self.action_dict = actionDict

    def lookupActions(self, rootNode):
        return self.action_dict[rootNode]

    def performActionOnRootState(self, rootNode):
        raise NotImplmentedError
