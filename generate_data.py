import numpy as np
import copy


def generate_sudoku(rmnum, datanum) -> dict:
    solution = [[2, 1, 4, 3], [3, 4, 1, 2], [1, 2, 3, 4], [4, 3, 2, 1]]
    data = {'puzzles': [], 'solution': []}
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
        data['solution'].append(solution)
    return data
