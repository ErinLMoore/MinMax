class State(object):
    #RESULT(s, a): The transition model, which defines the result of a move.
    #terminal test
    #utility of a state based on states under it
    def findPossibleActions(self):
        raise NotImplementedError
