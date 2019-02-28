from slideshow import Slideshow
from slide import Slide
from MergeVertical import preprocess_pictures


def get_slideshow(pictures):
    slides = preprocess_pictures(pictures)
    sorted_slides = sort_slides(slides)
    slideshow = setup_slideshow(sorted_slides)
    return slideshow


def sort_slides(slides):
    sorted_slides = slides.sort(key=lambda x: len(x.tags), reverse=True)
    return sorted_slides


def setup_slideshow(slides):
    slideshow = Slideshow()
    base_slide = slides.pop(0)
    slideshow.add_slide(base_slide)
    while slides:
        best_slide = 0
        count = 0
        for follow_slide in slides[1:-1]:
            if count == 100:
                base_slide = slides.pop(best_slide)
                slideshow.add_slide(base_slide)
                break
            count += 1

            tags_equal = len(slides[0].tags.intersection(follow_slide.tags))
            tags_size = len(slides[0].tags)

            if tags_size / 2 - 3 <= tags_equal <= tags_size / 2 + 3:
                best_slide = count

    return slideshow
