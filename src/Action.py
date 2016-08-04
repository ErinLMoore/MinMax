import src.ResultantState
import numpy as np

class Action(object):
    #returns the set of legal moves in a stat(e

    def __init__(self, actionDict):
        self.action_dict = actionDict

    def lookupActions(self, rootNode):
        raise NotImplementedError
