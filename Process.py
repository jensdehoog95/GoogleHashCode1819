from slideshow import Slideshow
from slide import Slide
from MergeVertical import preprocess_pictures


def get_slideshow(pictures):
    slides = preprocess_pictures(pictures)
    sort_slides(slides)
    slideshow = setup_slideshow(slides)
    return slideshow


def sort_slides(slides):
    slides.sort(key=lambda x: len(x.tags), reverse=True)


def setup_slideshow(slides):
    slideshow = Slideshow()
    base_slide = slides.pop(0)
    slideshow.add_slide(base_slide)
    while len(slides)>0:

        best_slide = 0
        for i in range(100):
            if(i>=len(slides)):
                break

            tags_equal = len(list(set(base_slide.tags) & set(slides[i].tags)))
            tags_size = len(slides[0].tags)

            if tags_size / 2 - 3 <= tags_equal <= tags_size / 2 + 3:
                best_slide = i
        base_slide = slides.pop(best_slide)
        slideshow.add_slide(base_slide)

    return slideshow
