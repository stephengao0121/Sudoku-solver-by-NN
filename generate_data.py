"""
generate_data.py: Utils to generate legal sudoku solutions and puzzles.
"""

import numpy as np
import copy
import random


def generate_sudoku(rmnum, datanum, solutions) -> dict:
    """
    Take the solutions and generate puzzles combined with solutions.
    :param rmnum: the number of digits is going to be eliminated from solution.
    :param datanum: the number of puzzles will be generated.
    :param solutions: the list of generated solutions.
    :return: a dictionary data {'puzzles': puzzle list, 'solutions': corresponding solutions}
    """
    data = {'puzzles': [], 'solutions': []}
    for solution in solutions:
        for k in range(datanum):
            puzzle = copy.deepcopy(solution)
            counter = 0
            while counter != rmnum:
                i = np.random.randint(4)
                j = np.random.randint(4)
                if puzzle[i][j] != 0:
                    puzzle[i][j] = 0
                    counter += 1
            data['puzzles'].append(puzzle)
            data['solutions'].append(solution)
    return data


def generate_solution() -> list:
    """
    A functions that generates legal sudoku solutions.
    :return: a list of solutions
    """
    def check_row_and_column(x, pos: tuple) -> bool:
        # check row.
        if x in solution[pos[0]]:
            return False

        # check column.
        trans = np.array(solution).T.tolist()
        if x in trans[pos[1]]:
            return False
        return True

    while True:
        solution = [[0 for i in range(4)] for j in range(4)]
        num_list = [1, 2, 3, 4]

        # fill the left-up square.
        random.shuffle(num_list)
        solution[0][0] = num_list[0]
        solution[0][1] = num_list[1]
        solution[1][0] = num_list[2]
        solution[1][1] = num_list[3]

        # fill the right-down square.
        random.shuffle(num_list)
        solution[2][2] = num_list[0]
        solution[2][3] = num_list[1]
        solution[3][2] = num_list[2]
        solution[3][3] = num_list[3]

        # fill the right-up square.
        random.shuffle(num_list)
        for i in range(0, 2):
            for j in range(2, 4):
                for k in num_list:
                    if check_row_and_column(k, (i, j)):
                        solution[i][j] = k
                        break

        # fill the left-down square.
        random.shuffle(num_list)
        for i in range(2, 4):
            for j in range(0, 2):
                for k in num_list:
                    if check_row_and_column(k, (i, j)):
                        solution[i][j] = k
                        break
        # check if valid solution.
        if np.array(solution).all():
            break
    return solution
