from slideshow import Slideshow
from slide import Slide
from MergeVertical import preprocess_pictures
import random


def get_slideshow(pictures, searchlength, difference, sort):
    slides = preprocess_pictures(pictures)
    if sort==0:
        sort_slides(slides)
    if sort == 1:
        random_sort(slides)
    if sort == 2:
        pass
    slideshow = setup_slideshow(slides, searchlength, difference)
    return slideshow


def sort_slides(slides):
    slides.sort(key=lambda x: len(x.tags), reverse=True)

def random_sort(slides):
    random.shuffle(slides)


def setup_slideshow(slides, searchlength, difference):
    slideshow = Slideshow()
    base_slide = slides.pop(0)
    slideshow.add_slide(base_slide)
    while len(slides)>0:

        best_slide = 0
        for i in range(searchlength):
            if(i>=len(slides)):
                break

            tags_equal = len(list(set(base_slide.tags) & set(slides[i].tags)))
            tags_size = len(slides[0].tags)

            if tags_size / 2 - difference <= tags_equal <= tags_size / 2 + difference:
                best_slide = i
        base_slide = slides.pop(best_slide)
        slideshow.add_slide(base_slide)

    return slideshow
