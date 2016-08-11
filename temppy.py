def fake_min(self, state):
      v = sys.maxsize
      if self.fake_terminal_test(state):
          return self.fake_calculate_utility_value(state)
      for a in self.fake_player1.return_possible_states(state):
          temp = self.max_value(a)
          if temp <  v:
              v = temp
      return v

  def fake_max(self, state):
      v = -sys.maxsize
      if self.fake_terminal_test(state):
          return self.fake_calculate_utility_value(state)
      for a in self.fake_player1.return_possible_states(state):
          temp = self.min_value(a)
          if temp >  v:
              v = temp
      return v
