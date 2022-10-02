from distutils.command.build_scripts import first_line_re
from turtle import down
from manim import *
class TreeScene(Scene):
    CONFIG={
        'iteraciones':3
    }
    def construct(self):
        ghost_line=Line(3*DOWN,4*DOWN).fade(1)
        self.first_line(ghost_line,)
    def first_line(self,path,angle=0,length=3):
        line=Line(UP,DOWN).rotate(angle).set_length(length)
        line.move_to(path.points[0],line.points[-1])
        line_left,line_right=line.copy(),line.copy()
        self.play(Create(line))
        self.wait()
        self.play(*[
            Rotate(
                mob,angle,about_point=line.points[0]
            ) for mob,angle in zip([line_left,line_right],[-140*DEGREES, 140*DEGREES])
        ])
        self.wait()