import numpy as np


class Board(object):

    def __init__(self, case: list):
        self._board = case

    def get_board(self):
        return self._board

    def check(self) -> bool:
        # count rows.
        for i in range(len(self._board)):
            if self._board[i].count(1) != 1 or self._board[i].count(2) != 1 \
                    or self._board[i].count(3) != 1 or self._board[i].count(4) != 1:
                return False

        # count columns.
        trans = np.array(self._board).T.tolist()
        for i in range(len(trans)):
            if trans[i].count(1) != 1 or trans[i].count(2) != 1 or trans[i].count(3) != 1 or trans[i].count(4) != 1:
                return False

        # count small squares.
        squares = self.parse_board()
        for i in range(len(squares)):
            if squares[i].count(1) != 1 or squares[i].count(2) != 1 \
                    or squares[i].count(3) != 1 or squares[i].count(4) != 1:
                return False

        return True

    def parse_board(self) -> list:
        # parse the board into 4 4*4 squares.
        parsed = [self._board[0][0: 2] + self._board[1][0: 2], self._board[0][2: 4] + self._board[1][2: 4],
                  self._board[2][0: 2] + self._board[3][0: 2], self._board[2][2: 4] + self._board[3][2: 4]]
        return parsed

    def find_possible_actions(self, pos: tuple):
        possible_acts = [1, 2, 3, 4]
        # check row.
        for i in possible_acts:
            if i in self._board[pos[0]]:
                possible_acts.remove(i)

        # check columns.
        trans = np.array(self._board).T.tolist()
        for i in possible_acts:
            if i in trans[pos[1]]:
                possible_acts.remove(i)

        # check small squares.
        squares = self.parse_board()
        if pos[0] < 2 and pos[1] < 2:
            squares = squares[0]
        elif pos[0] < 2 and pos[1] > 1:
            squares = squares[1]
        elif pos[0] < 2 and pos[1] > 1:
            squares = squares[2]
        else:
            squares = squares[3]
        for i in possible_acts:
            if i in squares:
                possible_acts.remove(i)

        return possible_acts
