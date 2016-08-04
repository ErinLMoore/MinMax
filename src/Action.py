import src.ResultantState

class Action(object):
    #returns the set of legal moves in a stat(e

    def __init__(self, actionDict):
        self.action_dict = actionDict

    def array_to_tuple(self, array):
        return tuple([tuple(i) for i in tuple(array)])

    def lookupActions(self, rootNode):
        return self.action_dict[]

    def performActionOnRootState(self, rootNode):
        raise NotImplmentedError
