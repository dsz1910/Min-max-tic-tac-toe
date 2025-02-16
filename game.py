import pygame
from tic_tac_toe_board import GameBoard
from minimax import MiniMax
from time import sleep



class Game:

    def __init__(self):
        pygame.init()
        self.running = True
        self.window = pygame.display.set_mode((GameBoard.width, GameBoard.height))
        pygame.display.set_caption('Tic-Tac-Toe')
        self.board = GameBoard(self.window)
        self.game_state = [[None, None, None], [None, None, None], [None, None, None]]
        self.start_turn = 'x'
        self.turn = self.start_turn
        self.winner = None
        self.draw_everything()

    def draw_everything(self):
        self.board.draw_board()
        self.board.draw_figures(self.game_state)
        self.board.draw_turn(self.turn)

    def x_turn(self, row, col):
        if self.game_state[row][col] is None:
            self.game_state[row][col] = -1
            self.turn = 'o'
            self.draw_everything()
    
    def circle_turn(self):
       state_copy = self.deep_copy()
       opponent = MiniMax(state_copy)
       r, c = opponent.ai_move()
       self.game_state[r][c] = 1
       self.turn = 'x'
       self.draw_everything()

    def deep_copy(self):
        return [[el for el in row] for row in self.game_state]
    
    def prepare_new_game(self):
        self.winner = None
        self.game_state = [[None, None, None], [None, None, None], [None, None, None]]
        if self.start_turn == 'x':
            self.start_turn = 'o'
        else:
            self.start_turn = 'x'
        self.turn = self.start_turn

    def print_winner(self):
        self.board.draw_board()
        if self.winner == -1:
            self.board.draw_x((1, 1))
            print('Wygrał X')
        elif self.winner == 0:
            self.board.draw_tie()
            print('Remis')
        else:
            self.board.draw_circle((1, 1))
            print('Wygrało kółko')
        self.board.draw_how_to_start()

    def check_winner(self):
        if self.game_state[1][1] is not None and (self.game_state[0][2] == self.game_state[1][1] == self.game_state[2][0] or self.game_state[0][0] == self.game_state[1][1] == self.game_state[2][2]):
            self.winner = self.game_state[1][1]
            return True

        for i in (-1, 1): 
            for j in range(3):
                if all(self.game_state[k][j] == i for k in range(3)) or all(self.game_state[j][c] == i for c in range(3)):
                    self.winner = i
                    return True

        if self.winner is None and not any(None in row for row in self.game_state):
            self.winner = 0
            return True
        
        return None
    
    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                elif self.winner is not None:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.prepare_new_game()
                        self.draw_everything()

                else:
                    if self.turn == 'o':
                        self.circle_turn()
                    else:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.winner is None:
                            x, y = event.pos
                            row = int(y // GameBoard.box_height)
                            col = int(x // GameBoard.box_width)
                            self.x_turn(row, col)
                    
                    self.check_winner()
                    if self.winner is not None:
                        pygame.display.update()
                        sleep(0.2)
                        self.print_winner()

            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()