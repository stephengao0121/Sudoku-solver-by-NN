import boardenv as bd


def main():
    inp = [[0, 0, 0, 0], [0, 4, 3, 0], [0, 0, 2, 1], [0, 0, 0, 0]]
    board = bd.Board(case=inp)
    board.train()
    board.solve()
    board.display()


if __name__ == '__main__':
    main()
