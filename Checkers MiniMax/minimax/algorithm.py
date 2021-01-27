from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255,255,255)

#Position holds the current board
#Depth is to control how long the tree will be
#max_player is boolean and tells us if we are maximising or minimising
#Game is the game object

def minimax(position, depth, max_player, game):
    #If we have reached the final level of the tree
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    #Maximise score
    if max_player:
        maxEval = float('-inf')
        best_move = None
        
        for move in get_all_moves(position, WHITE, game): #For every move possible, evaluate the moves recursivly
            evaluation = minimax(move, depth-1, False, game)[0] 
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation: #Store the best move
                best_move = move
        
        return maxEval, best_move
        
    else: # Minimise score
        minEval = float('inf')
        best_move = None
        
        for move in get_all_moves(position, RED, game): #For every move possible, evaluate the moves recursivly
            evaluation = minimax(move, depth-1, True, game)[0] 
            minEval = min(minEval, evaluation)
            if minEval == evaluation: #Store the best move
                best_move = move
        
        return minEval, best_move  

#Returns the new board after a move
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
        
    return board
      
        
        
#Return all possible moves from current position    
def get_all_moves(board, colour, game):
    moves = [] #Stores new board after a piece has been moved
    
    for piece in board.get_all_pieces(colour):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board) #Dont want to override current board
            temp_piece = temp_board.get_piece(piece.row, piece.col) #Need a copy of the pieces
            new_board = simulate_move(temp_piece, move, temp_board, game, skip) #Stores new board after a move
            moves.append(new_board)            
            
    return moves 


#def draw_moves(game, board, piece):
#    valid_moves = board.get_valid_moves(piece)
#    board.draw(game.win)
#    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
#    game.draw_valid_moves(valid_moves.keys())
#    pygame.display.update()
    
    
    