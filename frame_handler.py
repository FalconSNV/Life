from random import randint
from objects import Cell


class FrameHandler:

    @staticmethod
    def make_map(size: int, first_gen_percent: float | int) -> list:
        """Создание матрицы клеток"""
        map_1 = [[] for i in range(size)]
        for i in range(size):
            for j in range(size):
                x = randint(1, 100)
                status = False
                if x < first_gen_percent:
                    status = True
                map_1[i].append(Cell(i, j, status))
        return map_1

    @staticmethod
    def cells_status(size: int, map_1: list, draw):
        """Вывод состояния клеток"""
        for i in range(size):
            for j in range(size):
                if map_1[i][j].accept():
                    color = (255, 255, 255)

                else:
                    color = (0, 0, 0)
                draw.point([i, j], color)

    @staticmethod
    def cells_conditions(size: int, map_1: list):
        """Оценка условий клеток"""
        for i in range(size):
            for j in range(size):
                map_1[i][j].check(map_1)
