# Tic Tac Toe board representation
class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |') 
            

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
      
    def winner(self, player):
        # Winning combinations of spots
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        # Check if any combination forms a win
        for combo in win_combinations:
            if all([self.board[i] == player for i in combo]):
                return True
        return False

    def game_over(self):
        return self.winner('X') or self.winner('O') or len(self.available_moves()) == 0

    def value(self):
        if self.winner("X"):
            return -1  # Jugador 'X' gana, por lo que el valor es negativo
        elif self.winner("O"):
            return  1  # Jugador 'O' gana, por lo que el valor es positivo
        else:
            return  0  # No hay ganador, por lo que el valor es cero
        

def ai_move(board):
    """
    Returns the optimal action for the current player on the board using the minimax algorithm.
    """
    def minimax(newBoard, depth, maximizingPlayer):
        if newBoard.game_over():
            return newBoard.value(), None

        if maximizingPlayer:
            maxEval = float('-inf')
            bestMove = None
            for move in newBoard.available_moves():
                newBoard.board[move] = 'O'
                evaluation = minimax(newBoard, depth +  1, False)[0]
                newBoard.board[move] = ' '
                if evaluation > maxEval:
                    maxEval = evaluation
                    bestMove = move
            return maxEval, bestMove
        else:
            minEval = float('inf')
            bestMove = None
            for move in newBoard.available_moves():
                newBoard.board[move] = 'X'
                evaluation = minimax(newBoard, depth +  1, True)[0]
                newBoard.board[move] = ' '
                if evaluation < minEval:
                    minEval = evaluation
                    bestMove = move
            return minEval, bestMove

    _, bestMove = minimax(board,  0, True)
    board.board[bestMove] = 'O'
                
def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move in board.available_moves():
                board.board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

# Main function to start the game
def main():
    board = Board()
    while not board.game_over():
        board.print_board()
        human_move(board)
        if not board.game_over():
            ai_move(board)
    board.print_board()
    if board.winner('X'):
        print("Congratulations! You won!")
    elif board.winner('O'):
        print("The CPU has won!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()


