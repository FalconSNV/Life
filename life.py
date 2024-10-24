import time

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from PIL import Image, ImageDraw
import imageio
import os
from frame_handler import FrameHandler


class Life:

    @staticmethod
    def start(size: int, first_gen_percent: float | int = 33, frames_cnt: int = 10):
        """Запуск 'Жизни'"""
        if not os.path.exists("images"):
            os.mkdir("images")
        for image in os.listdir("images"):
            os.remove("images/"+image)
        map_ = Image.new("RGB", (size, size), "black")
        draw = ImageDraw.Draw(map_)
        map_1 = FrameHandler.make_map(size, first_gen_percent)
        for z in range(frames_cnt):
            FrameHandler.cells_status(size, map_1, draw)
            map_.save(f"images/img-{z}.png")
            FrameHandler.cells_conditions(size, map_1)

    @staticmethod
    def save(fps: int = 2, format: str = "GIF"):
        """Сохранение GIF или mp4 файла"""
        frames = []
        for i in range(len(os.listdir("images"))):
            frames.append(Image.open(f"images/img-{i}.png", "r"))
        if format == "GIF":
            frames[0].save(
                'life.gif',
                save_all=True,
                append_images=frames[1:],
                optimize=True,
                duration=1000/fps
            )
        elif format == "mp4":
            with imageio.get_writer('animation.mp4', mode='I', fps=2) as writer:
                for img in frames:
                    writer.append_data(np.array(img))
