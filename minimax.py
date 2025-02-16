from random import shuffle, choice


class MiniMax:

    def __init__(self, state) -> None:
        self.state = state
        self.best_move = None

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, val):
        if isinstance(val, list)  and len(val) == 3 and all([x in (None, 1, -1) for x in row] for row in val) and all([len(row) == 3 for row in val]):
            self._state = val

    @property
    def best_move(self):
        return self._best_move
    
    @best_move.setter
    def best_move(self, val):
        if (isinstance(val, tuple) and len(val) == 2 and all(isinstance(x, int) for x in val) and all(0 <= x < 3 for x in val)) or val is None:
            self._best_move = val

    def check_possible_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.state[r][c] is None]
    
    def terminal_state(self):
        if self.state[1][1] is not None and (self.state[0][2] == self.state[1][1] == self.state[2][0] or self.state[0][0] == self.state[1][1] == self.state[2][2]):
            return self.state[1][1]

        for j in range(3):
            if self.state[j][0] is not None and all(self.state[j][c] == self.state[j][0] for c in range(3)):
                return self.state[j][0]
            if self.state[0][j] is not None and all(self.state[r][j] == self.state[0][j] for r in range(3)):
                return self.state[0][j]

        if len(self.check_possible_moves()) == 0:
            return 0
        
        return None
    
    def minimax(self, max_turn):
        winner = self.terminal_state()
        if isinstance(winner, int):
            return winner
        
        possible_moves = self.check_possible_moves()
        shuffle(possible_moves)
        value = -10 if max_turn else 10

        for move in possible_moves:
            self.action(move, max_turn)
            move_value = self.minimax(not max_turn)
            self.undo_move(move)
            
            if max_turn:
                if move_value > value:
                    value = move_value
                    if value == 1:
                        return 1
            else:
                if move_value < value:
                    value = move_value
                    if value == -1:
                        return -1

        return value
    
    def action(self, pos, max_turn):
        if max_turn:
            self.state[pos[0]][pos[1]] = 1
        else:
            self.state[pos[0]][pos[1]] = -1
        
    def undo_move(self, pos):
        self.state[pos[0]][pos[1]] = None

    def ai_move(self):
        possible_moves = self.check_possible_moves()
        shuffle(possible_moves)

        if len(possible_moves) == 9:
            self.best_move = choice(possible_moves)
            return self.best_move
        
        value = -10
        for move in possible_moves:
            self.action(move, True)
            move_value = self.minimax(False)
            self.undo_move(move)

            if move_value > value:
                value = move_value
                self.best_move = move
                if value == 1:
                    break

        return self.best_move
    

if __name__ == '__main__':
    ai = MiniMax([[1,- 1, -1], [None, -1, 1], [None, None, None]])
    print(ai.ai_move())