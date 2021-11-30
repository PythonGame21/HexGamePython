from state_class import State
from random import randint


class EzII:
    @staticmethod
    def find_move(state):
        x = randint(0, len(state) - 1)
        y = randint(0, len(state[0]) - 1)
        while state[x][y] != State.FREE:
            x = randint(0, len(state) - 1)
            y = randint(0, len(state[0]) - 1)
        state[x][y] = State.P2


class HdII:

    @staticmethod
    def find_move(state, last):
        def in_bounds(pos):
            return 0 <= pos[0] < len(state) and 0 <= pos[1] < len(state[0])

        for i in range(len(state)):
            for j in range(len(state[0])):
                if (i, j) == last:
                    for dx in range(1, -2, -1):
                        for dy in range(-1, 2):
                            if dx == 0 and dy == 0 or abs(dx + dy) == 2 or not in_bounds((i+dx, j+dy)):
                                continue
                            if state[i+dx][j+dy] == State.FREE:
                                state[i + dx][j + dy] = State.P2
                                return
        EzII.find_move(state)
