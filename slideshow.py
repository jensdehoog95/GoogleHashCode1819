from slide import Slide

class Slideshow():
    def __init__(self):
        self.slides = []

    def add_slide(self, slide: Slide):
        self.slides.append(slide)

    def parse_output(self):
        pass