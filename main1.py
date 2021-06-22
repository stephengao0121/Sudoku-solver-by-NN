# ---------------------------------------------------------------
# Project:              Machine Learning on Sudoku
# Authors*:		DU Haoyu(Henry), GAO Lanhe(Stephen), HU Xiaoyue(Rebecca), LI Xinyi(Monica)
# Start Date:           6/20/2021
# End Date:             
# Copyright (c):        ST 8201-G3
# * All authors have contributed equally.
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# This project serves to develop possible machine learning algorithms
# for computers to solve sudoku alone without the assistance from
# human expertise.
# ---------------------------------------------------------------


class Board:
    # sudoku board contains integers and/or white space

    def __init__(self, board, dimension=4):
        self.__board = board              # pointer to sudoku
        self.__dimension = dimension      # number of rows
        self.__result = 0                 # 0 incomplete; 1 otherwise

    def print_board(self):
        # print the board to terminal
        # args: none
        # returns: none
        print("\n" + "-" * (self.__dimension * 4 + 1))
        for i in range(self.__dimension):
            print("|", end="")
            for j in range(self.__dimension):
                print(" {} |".format(self.__board[i][j]), end="")
            print("\n"+"-"*(self.__dimension * 4 + 1))

    def get_dimension(self):
        # return the dimension of sudoku
        # args: none
        # returns: dimension - int
        return self.__dimension

    def get_result(self):
        # return the result of sudoku
        # args: none
        # returns: result - int
        return self.__result

    def fill(self, row, col, num):
        # fill sudoku blanks
        # for convenience, index starts from 1
        # args: row - int: row index
        #       col - int: column index
        #       num - int: number to be filled in the blank
        # returns: 0 if failed; 1 if succeeded
        if row > self.__dimension or col > self.__dimension:
            print("[Error] Index out of range")
            return 0
        row -= 1
        col -= 1
        if self.__board[row][col] != " ":
            print("[Error] Cell not empty")
            return 0
        if type(num) != int:
            print("[Error] Input not integer")
            return 0
        self.__board[row][col] = num
        return 1

    def build_hashset(self):
        # create a hashset to check repetition in row/column/square
        # args: none
        # returns: hashset - dict
        hashset = {1: 0}                # hashset of possible integers
        for i in range(1, self.__dimension+1):
            hashset[i] = 0
        return hashset

    def check_rows(self):
        # check repetition in all rows
        # args: none
        # returns: 0 if repetition found; 1 otherwise
        for r in range(self.__dimension):
            hashset = self.build_hashset()
            for c in range(self.__dimension):
                if self.__board[r][c] != " ":
                    hashset[self.__board[r][c]] += 1
                    if hashset[self.__board[r][c]] > 1:
                        return 0
        return 1

    def check_cols(self):
        # check repetition in all columns
        # args: none
        # returns: 0 if repetition found; 1 otherwise
        for c in range(self.__dimension):
            hashset = self.build_hashset()
            for r in range(self.__dimension):
                if self.__board[r][c] != " ":
                    hashset[self.__board[r][c]] += 1
                    if hashset[self.__board[r][c]] > 1:
                        return 0
        return 1


def main():
    sudoku = [[2, " ", 4, " "],
         [3, 4, 1, " "],
         [" ", " ", " ", 4],
         [4, 3, " ", " "]]
    board = Board(sudoku)
    board.print_board()


main()
