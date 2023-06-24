from manim import *


class FirstExample(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)  # 一个蓝色的不透明度为0.9的圆
        green_square = Square(color=GREEN, fill_opacity=0.8)
        green_square.next_to(blue_circle, RIGHT)  # 绿色的正方形在紧挨在蓝色圆的右边，若无位置设置物体默认在舞台的中央
        self.add(blue_circle, green_square)  # 将圆和正方形加入的舞台上
