from manim import *
class TreeScene(Scene):
    CONFIG={
        'iteraciones':5
    }
    def construct(self):
        ghost_line=Line(3*DOWN,4*DOWN).fade(1).center()
        self.first_line(ghost_line)
        for _ in range(self.CONFIG['iteraciones']):
            self.first_line(self.line_left,-PI/2+self.line_left.get_angle(),self.line_left.get_length()/2)
    def first_line(self,path,angle=0,length=3):
        line=Line(UP,DOWN).rotate(angle).set_length(length)
        line.move_to(path.points[-1],line.points[0])
        self.line_left,self.line_right=line.copy(),line.copy()
        self.play(Create(line))
        self.play(*[
            Rotate(
                mob,angle,about_point=line.points[0]
            ) for mob,angle in zip([self.line_left,self.line_right],[-140*DEGREES, 140*DEGREES])
        ])
    def first_line_2(self,path,angle=0,length=3):
        line=Line(UP,DOWN).rotate(angle).set_length(length)
        line.move_to(path.points[-1],line.points[0])
        self.line_left,self.line_right=line.copy(),line.copy()
        self.play(Create(line))
        self.play(*[
            Rotate(
                mob,angle,about_point=line.points[0]
            ) for mob,angle in zip([self.line_left,self.line_right],[-140*DEGREES, 140*DEGREES])
        ])