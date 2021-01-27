import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from .board import Board

class Game:
    def __init__(self,win):
        self._init()
        self.win = win
        
    #Display new board after a move
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()        
     
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}        

    def reset(self):
        self._init()
        
    def winner(self):
        return self.board.winner()

    #Checks and moves a piece to an empty square if possible
    #If a piece is selected then get the valid moves
    def select(self,row,col):
        if self.selected :
            result = self._move(row,col)
            #If unable to move to square 
            if not result:
                self.selected = None
                self.select(row,col)
                
        piece = self.board.get_piece(row,col)
        #If we have selected our own piece
        if piece !=0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False           
        
    #Moves the piece to an empty square and removes oppositions pieces which have been jumped  
    def _move(self,row,col):
        piece = self.board.get_piece(row,col)
        #If we selected an empty square 
        if self.selected and piece ==0 and (row,col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row,col)]         
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            
        else:
            return False
        return True
    
    #Draws circles to where the player can move
    def draw_valid_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2 ), 15)
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED            

    def get_board(self):
        return self.board
    
    #Return updated board after AI move
    def ai_move(self,board):
        self.board = board
        self.change_turn()
        
    