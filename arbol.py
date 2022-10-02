from manim import *
import itertools as it
class TreeScene(Scene):
    CONFIG={
        'iteraciones':4
    }
    def construct(self):
        first_path=Line(2*DOWN,ORIGIN)
        second_line=Line()
        self.play(Create(first_path))
        for _ in range(self.CONFIG['iteraciones']):
            p1,p2=first_path.copy(),first_path.copy()
            group=VGroup(p1,p2)
            group.move_to(second_line.points[0],group[0].points[0])
            p1.rotate(60*DEGREES)
            p2.rotate(-60*DEGREES)
            self.play(
                ReplacementTransform(first_path,p1),
                ReplacementTransform(first_path.copy(),p2)
            )
            first_path=VGroup(*it.chain(p1,p2))
        self.wait()