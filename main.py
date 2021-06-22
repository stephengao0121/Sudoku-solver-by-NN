import numpy as np
import boardenv as bd
import nn
import generate_data as gd
import tensorflow.keras as kr


def main():
    # Generate data and its one-hot coding.
    data = gd.generate_sudoku(0, 1)
    x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
    y_train = kr.utils.to_categorical(np.array(data['solution'][:]) - 1)

    # Generate model and model fitting.
    model = nn.SudokuNN(input_shape=(4, 4, 5), layer_num=1, mid_num=9)
    model.compile()
    model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

    data = gd.generate_sudoku(1, 15)
    x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
    y_train = kr.utils.to_categorical(np.array(data['solution'][:]) - 1)
    model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

    data = gd.generate_sudoku(2, 80)
    x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
    y_train = kr.utils.to_categorical(np.array(data['solution'][:]) - 1)
    model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

    data = gd.generate_sudoku(3, 500)
    x_train = kr.utils.to_categorical(np.array(data['puzzles'][:]))
    y_train = kr.utils.to_categorical(np.array(data['solution'][:]) - 1)
    model.fit(x_train, [y_train[:, i, j, :] for i in range(4) for j in range(4)], batch_size=1, epochs=1)

    data = gd.generate_sudoku(10, 100)
    x_test = np.array(data['puzzles'][:])

    correct = 0
    total = len(x_test)
    prediction = np.array(model.predict(kr.utils.to_categorical(x_test)))
    values = (prediction.argmax(2).T + 1).tolist()
    solution = [[2, 1, 4, 3, 3, 4, 1, 2, 1, 2, 3, 4, 4, 3, 2, 1]]

    for i in range(len(values)):
        flat_test = x_test[i].reshape(-1, 16).tolist()
        # print(flat_test)
        # print(values[i])

        for j in range(len(flat_test[0])):
            if flat_test[0][j] == 0:
                flat_test[0][j] = values[i][j]
        if flat_test == solution:
            correct += 1

    print('accuracy is {}'.format(correct/total))


if __name__ == '__main__':
    main()
