from state_class import State
from random import randint
from collections import deque


class EzII:
    @staticmethod
    def do_move(state, move_his):
        x = randint(0, len(state) - 1)
        y = randint(0, len(state[0]) - 1)
        while state[x][y] != State.FREE:
            x = randint(0, len(state) - 1)
            y = randint(0, len(state[0]) - 1)
        state[x][y] = State.P2
        move_his.append((x, y))


class HdII:
    def __init__(self, state, his):
        self.state = state
        self.his = his

    def update(self, state, his):
        self.state = state
        self.his = his

    def in_bounds(self, pos):
        return 0 <= pos[0] < len(self.state) and 0 <= pos[1] < len(self.state[0])

    def do_move(self):
        m = self.one_m_win()
        if m != None:
            self.his.append(m)
            return
        for i in self.his[::-2]:
            m = self.f_m_point(i)
            if m != None:
                self.his.append(m)
                return
        EzII.do_move(self.state, self.his)

    def f_m_point(self, p1m):
        return self.check_around(p1m)

    def check_around(self, p1m):
        x = p1m[0]
        y = p1m[1]
        if self.in_bounds((x + 1, y - 1)):
            if self.state[x + 1][y - 1] == State.FREE and self.state[x + 1][y] == State.FREE:
                if self.in_bounds((x + 2, y - 1)) and self.state[x + 2][y - 1] == State.FREE:
                    self.state[x + 2][y - 1] = State.P2
                    return (x+2, y-1)
            if self.state[x + 1][y - 1] == State.P2 and self.state[x + 1][y] == State.FREE:
                self.state[x + 1][y] = State.P2
                return (x+1, y)
            if self.state[x + 1][y - 1] == State.FREE and self.state[x + 1][y] == State.P2:
                self.state[x + 1][y - 1] = State.P2
                return (x+1, y-1)
        elif self.in_bounds((x + 1, y)) and self.state[x + 1][y] == State.FREE:
            self.state[x + 1][y] = State.P2
            return (x+1, y)
        if self.in_bounds((x - 1, y + 1)):
            if self.state[x - 1][y] == State.FREE and self.state[x - 1][y + 1] == State.FREE:
                if self.in_bounds((x - 2, y + 1)) and self.state[x - 2][y + 1] == State.FREE:
                    self.state[x - 2][y + 1] = State.P2
                    return (x-2, y+1)
            if self.state[x - 1][y] == State.P2 and self.state[x - 1][y + 1] == State.FREE:
                self.state[x - 1][y + 1] = State.P2
                return (x-1, y+1)
            if self.state[x - 1][y] == State.FREE and self.state[x - 1][y + 1] == State.P2:
                self.state[x - 1][y] = State.P2
                return (x-1, y)
        elif self.in_bounds((x - 1, y)) and self.state[x - 1][y] == State.FREE:
            self.state[x - 1][y] = State.P2
            return (x-1, y)
        return None

    def one_m_win(self):
        state = self.state

        def in_bounds(x, y):
            return 0 <= x < len(state) and 0 <= y < len(state[0])

        def DFS_is_win(state, visited, p, w_c, m, globs):
            if globs[0]:
                return
            if p[1] == w_c:
                globs[0] = True
                globs[1] = m
                return
            visited = visited.copy()
            visited.add((p[0], p[1]))
            x = p[0]
            y = p[1]
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0 or abs(dx + dy) == 2 or not in_bounds(x + dx, y + dy):
                        continue
                    if state[x + dx][y + dy] == State.P2 and (x + dx, y + dy) not in visited:
                        DFS_is_win(state, visited, (x + dx, y + dy), w_c, m, globs)
                    elif state[x + dx][y + dy] == State.FREE and m is None:
                        DFS_is_win(state, visited, (x + dx, y + dy), w_c, (x + dx, y + dy), globs)

        for x in range(len(state)):
            if state[x][0] == State.P2:
                visited = set()
                globs = [False, None]
                DFS_is_win(state, visited, (x, 0), len(state[0]) - 1, None, globs)
                if globs[0]:
                    state[globs[1][0]][globs[1][1]] = State.P2
                    return (globs[1][0], globs[1][1])
            if state[x][-1] == State.P2:
                visited = set()
                globs = [False, None]
                DFS_is_win(state, visited, (x, len(state[0]) - 1), 0, None, globs)
                if globs[0]:
                    state[globs[1][0]][globs[1][1]] = State.P2
                    return (globs[1][0], globs[1][1])
        return None

