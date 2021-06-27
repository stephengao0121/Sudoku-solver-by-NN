import boardenv as bd
import pygame

def main():
    inp = [[2, 0, 4, 0], [3, 4, 1, 0], [0, 0, 0, 4], [4, 3, 0, 0]]
    board = bd.Board(case=inp)
    board.train()
    board.solve()
    board.display()
    Sudoku = board.outcome()

    # Use pygame to visualize the Sudoku board

    # init pygame
    pygame.init()

    # contant
    SIZE = [400, 450]
    font40 = pygame.font.SysFont('Times', 40)
    font15 = pygame.font.SysFont('Times', 15)

    # create screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Sudoku-Group 3")

    # main loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # draw background
        # white background
        backgroud = (255, 255, 255)
        screen.fill(backgroud)

        # draw game board
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 200, 400), 3)
        pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 400), 1)
        pygame.draw.rect(screen, (0, 0, 0), (200, 0, 200, 400), 3)
        pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 400), 1)

        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 200), 3)
        pygame.draw.line(screen, (0, 0, 0), (0, 100), (400, 100), 1)
        pygame.draw.rect(screen, (0, 0, 0), (0, 200, 400, 300), 3)
        pygame.draw.line(screen, (0, 0, 0), (0, 300), (400, 300), 1)
        pygame.draw.line(screen, (0, 0, 0), (0, 450), (400, 450), 5)

        # draw numbers
        for i in range(len(Sudoku)):
            for j in range(len(Sudoku[0])):
                txt = font40.render(str(Sudoku[i][j] if Sudoku[i][j] not in [0, '0'] else ''), True, (0, 0, 0))
                x, y = j * 100 + 40, i * 100 + 35
                screen.blit(txt, (x, y))

        #give context
        txt1 = font15.render(('Group 3 Project: Sudoku '), True, (0, 0, 0))
        txt2 = font15.render(('Members: Steph, Henry, Rebecca, Monica'), True, (0, 0, 0))
        x, y = 10, 408
        x1, y1 = 10, 430
        screen.blit(txt1, (x, y))
        screen.blit(txt2, (x1, y1))

        # flip
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()