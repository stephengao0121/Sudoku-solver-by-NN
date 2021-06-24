"""
boardenv.py: Board class declaration and definitions.
"""

import numpy as np
import nn
import generate_data as gd
import tensorflow.keras as kr


class Board(object):

    def __init__(self, case: list):
        """
        Constructor function
        :param case: The puzzle needed to be solve.
        """
        self._board = case
        self._model = nn.SudokuNN(input_shape=(4, 4, 5), layer_num=3, mid_num=20)
        self._model.compile()

    def get_board(self) -> list:
        """
        Get the board status.
        :return: The current board digits.
        """
        return self._board

    def set_board(self, board: list):
        """
        Set the _board as board
        :param board: The board that is going to be set.
        :return: None
        """
        self._board = board

    def check(self) -> bool:
        """
        Check the board is a legal solution.
        :return: Boolean. Whether legal or illegal.
        """
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
        """
        A functions used to parse the board into small squares. Used in check().
        :return: A list of parsed board.
        """
        # parse the board into 4 4*4 squares.
        parsed = [self._board[0][0: 2] + self._board[1][0: 2], self._board[0][2: 4] + self._board[1][2: 4],
                  self._board[2][0: 2] + self._board[3][0: 2], self._board[2][2: 4] + self._board[3][2: 4]]
        return parsed

    def display(self):
        """
        Visualization functions.
        :return: None
        """
        print("\n" + "-" * (len(self._board) * 4 + 1))
        for i in range(len(self._board)):
            print("|", end="")
            for j in range(len(self._board)):
                print(" {} |".format(self._board[i][j]), end="")
            print("\n"+"-"*(len(self._board) * 4 + 1))

    def train(self):
        """
        A function that lets the board to train its model.
        :return: None
        """
        # Generate data and its one-hot coding, then fit the model.
        solutions = [gd.generate_solution() for i in range(250)]
        data = gd.generate_sudoku(0, 1, solutions)
        x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

        data = gd.generate_sudoku(1, 15, solutions)
        x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

        data = gd.generate_sudoku(2, 50, solutions)
        x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

        data = gd.generate_sudoku(3, 50, solutions)
        x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

        data = gd.generate_sudoku(4, 50, solutions)
        x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

        data = gd.generate_sudoku(5, 50, solutions)
        x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

        # data = gd.generate_sudoku(6, 100, solutions)
        # x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        # y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        # self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)
        #
        # data = gd.generate_sudoku(7, 100, solutions)
        # x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        # y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        # self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)
        #
        # data = gd.generate_sudoku(8, 1000, solutions)
        # x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        # y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        # self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)
        #
        # data = gd.generate_sudoku(9, 1000, solutions)
        # x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
        # y_train = kr.utils.to_categorical(np.array(data['solutions'][:]) - 1)
        # self._model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

    def solve(self):
        """
        Let the trained model to solve the puzzle.
        :return: None
        """
        test = np.array(self._board)
        for _ in range((test == 0).sum((0, 1)).max()):
            # make predictions, then take the value with the maximum likelihood.
            prediction = np.array(self._model.predict(kr.utils.to_categorical([test])))
            probabilities = prediction.max(2).T
            values = prediction.argmax(2).T + 1
            zeros = (test == 0).reshape(-1, 16)

            # replace one 0 with the most confident value in this prediction.
            if np.any(zeros[0]):
                where = np.where(zeros[0])[0]
                confidence_position = where[probabilities[0][zeros[0]].argmax()]  # pos with highest prob.
                confidence_value = values[0][confidence_position]
                test.flat[confidence_position] = confidence_value

        self._board = test.reshape(4, 4).tolist()
