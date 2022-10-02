from tokenize import group
from manim import *
import itertools as it
class PointsScene(Scene):
    CONFIG={
        
    }
    def construct(self):
        first_position=np.array([
            np.random.uniform(-config['frame_width']/2,config['frame_width']/2),
            np.random.uniform(-config['frame_height']/2,config['frame_height']/2),
            0,
        ])
        dot=Dot(radius=.05).move_to(first_position)
        self.get_points(dot)
        self.wait()
    def get_points(self,dot):
        for i in it.count():
            if i==7:
                break
            position_1=np.array([
                np.random.uniform(-config['frame_width']/2,config['frame_width']/2),
                np.random.uniform(-config['frame_height']/2,config['frame_height']/2),
                0,
            ])
            position_2=np.array([
                np.random.uniform(-config['frame_width']/2,config['frame_width']/2),
                np.random.uniform(-config['frame_height']/2,config['frame_height']/2),
                0,
            ])
            d1,d2=dot.copy(),dot.copy()
            d1.move_to(position_1)
            d2.move_to(position_2)
            group=VGroup(d1,d2)
            self.play(
                TransformFromCopy(dot,d1),
                TransformFromCopy(dot.copy(),d2)
            )
            dot=VGroup(*it.chain(d1,d2))
        def get_beam(self,points):
            beam=VMobject()
            beam.set_points_as_corners(points)
            beam.set_stroke(BLUE_B,2)
            anims=[self.get_beam_anim(beam)]
            self.play(*anims)
        def get_beam_anim(self,beam):
            dot=Dot(radius=.05)
            return AnimationGroup(
                ShowPassingFlash(
                    beam,
                    run_time=5,
                    rate_func=lambda t: smooth(t,5),
                    time_width=0.05
                ),
                UpdateFromFunc(
                    dot,
                    lambda m: m.move_to(beam.points[-1])
                )
            )
            