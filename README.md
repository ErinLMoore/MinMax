MinMax

Notes on Numpy:

oh if you do from numpy import * you don't have to put numpy.
statevector = numpy.array([[ 1.],
                [ 0.],
                [ 0.]])

IdentityMatrix = numpy.eye(3)

IdentityMatrix.dot(statevector)
>>>

state_one = State(self.win_state)
state_one.get_utility = self.fake_return_it(1)

todo: stub and mock the function that determines the worth of
of a terminal state
