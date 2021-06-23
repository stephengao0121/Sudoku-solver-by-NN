import boardenv as bd


def main():
    inp = [[0, 0, 0, 4], [0, 4, 3, 0], [0, 0, 2, 1], [2, 0, 0, 3]]
    board = bd.Board(case=inp)
    board.train()
    board.solve()
    board.display()


if __name__ == '__main__':
    main()
