import unittest
import mock
from src.MinMax import minMax, State


class test_MinMax(unittest.TestCase):

    def setUp(self):
        minmax = minMax

    def test_noPossibleActions(self):
        state = ''
        expected = None
        actual = minmax.bestActionFromState(state)
        self.assertEqual(expected, actual)

    def mockreturnAState(self):
        state1 = State()
        return state1


    def mockfindPossibleActions(self):
        action1 = Action()
        action2 = Action()
        action3 = Action()
        return [action1, action2, action3]

    def test_maximizedActionIsTaken(self):
        originalstate = State()
        originalstate.findPossibleActions = self.mockfindPossibleActions()
        action1.returnAState = self.returnAState()
        action2.returnAState = self.returnAState()
        action3.returnAState = self.returnAState()
        utilityObtained = Action.getStateUtility()
        
        expected = Action.getStateUtility()
        actual = minMax.bestActionFromState(state)
        self.assertEqual(expected, actual)
