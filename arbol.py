from turtle import pos
from manim import *
class TreeScene(Scene):
    CONFIG={
        'iteraciones':5,
        'angle':40*DEGREES,
    }
    def construct(self):
        first_path=Line(ORIGIN,3*DOWN)
        first_path.angle=0*DEGREES
        first_path.length=first_path.get_length()
        PATHS=VGroup()
        self.play(Create(first_path))
        line_left, line_right=self.getting_branch(first_path)
        self.play(Create(line_left),Create(line_right))
        PATHS.add(line_left,line_right)
        line_left=self.getting_branch(line_left)
        line_right=self.getting_branch(line_right)
        self.play(Create(line_left),Create(line_right))
        self.play(Create(line_left),Create(line_right))
        self.wait()
    def getting_branch(self,path):
        line_left=path.copy()
        line_right=path.copy()
        line_left.set_length(path.length/2)
        line_right.set_length(path.length/2)
        line_left.move_to(path.points[0],line_left.points[-1])
        line_right.move_to(path.points[0],line_right.points[-1])
        line_left.rotate(
            angle=path.angle-self.CONFIG['angle']+2*PI,
            about_point=path.points[0]
        )
        line_right.rotate(
            angle=path.angle+self.CONFIG['angle']-2*PI,
            about_point=path.points[0]
        )
        return VGroup(line_left,line_right)