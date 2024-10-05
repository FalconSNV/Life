class Cell:
    """Объект описывающий поведение отдельной клетки"""

    def __init__(self, x: int, y: int, alive: bool):
        self.alive = alive
        self.x = x  # координата x
        self.y = y  # координата y
        self.memory = alive

    def check(self, atoms: list) -> None:
        """Подсчет числа живых клеток вокруг"""
        alive_count = 0
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    try:
                        if atoms[self.x+i-1][self.y+j-1].alive:
                            alive_count += 1
                    except IndexError:
                        pass
        if alive_count < 2 or alive_count > 3:
            self.memory = False
        elif alive_count == 3:
            self.memory = True

    def accept(self) -> bool:
        """Определение состояния клетки"""
        self.alive = self.memory
        if self.alive:
            return True
        else:
            return False
