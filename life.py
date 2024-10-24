from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from random import randint
from objects import Cell


class Life:

    @staticmethod
    def start(size: int, first_gen_percent: float | int = 33, frame_interval: int = 100):
        """Запуск 'Жизни'"""
        fig, ax = plt.subplots()
        fig.canvas.manager.full_screen_toggle()
        map_1 = [[] for i in range(size)]
        map_2 = np.zeros((size, size))
        ax.set_title("LIFE (ALT+F4 to escape)")
        im = ax.imshow(map_2, cmap='gray', vmin=0, vmax=1)
        for i in range(size):
            for j in range(size):
                x = randint(1, 100)
                status = False
                if x < first_gen_percent:
                    status = True
                map_1[i].append(Cell(i, j, status))
        for i in range(size):
            for j in range(size):
                map_2[i][j] = map_1[i][j].accept()

        def animate(frame):
            for i in range(size):
                for j in range(size):
                    map_1[i][j].check(map_1)
            for i in range(size):
                for j in range(size):
                    map_2[i][j] = map_1[i][j].accept()
            im.set_array(map_2)
            return im,

        anim = animation.FuncAnimation(fig, animate, frames=100, interval=frame_interval)
        plt.show()
