class State(object):
    #RESULT(s, a): The transition model, which defines the result of a move.
    #terminal test
    #utility of a state based on states under it
    def __init__(self, actionArray, Utility= None):
        self.actionArray = actionArray
        self.utility = Utility

    def get_actionArray(self):
        raise NotImplementedError

    def get_utility(self):
        raise NotImplementedError
