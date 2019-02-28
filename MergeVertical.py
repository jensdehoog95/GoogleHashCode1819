from slide import Slide
from photo import Photo


def preprocess_pictures(pictures, merge_type):
    vertical_pictures, horizontal_pictures = remove_vertical_pictures(pictures)

    merged_slides = []
    if merge_type == 0:
        merged_slides = merge_vertical_pictures(vertical_pictures)
    elif merge_type == 1:
        merged_slides = merge_vertical_pictures_high(vertical_pictures)
    slides = []
    slides.extend(merged_slides)
    for picture in horizontal_pictures:
        slides.append(Slide(picture))
    return slides


def merge_vertical_pictures(vertical_pictures):
    sort_pictures(vertical_pictures)
    merged_pictures = []
    while len(vertical_pictures) > 1:
        v1 = vertical_pictures.pop(0)
        v2 = vertical_pictures.pop(-1)

        slide = Slide(v1, v2)
        merged_pictures.append(slide)
    return merged_pictures


def merge_vertical_pictures_high(vertical_pictures):
    sort_pictures(vertical_pictures)
    merged_pictures = []
    while len(vertical_pictures) > 1:
        v1 = vertical_pictures.pop(0)
        v2 = vertical_pictures.pop(1)

        slide = Slide(v1, v2)
        merged_pictures.append(slide)
    return merged_pictures


def sort_pictures(vertical_pictures):
    vertical_pictures.sort(key=lambda x: len(x.tags), reverse=True)


def remove_vertical_pictures(pictures):
    vertical_pictures = []
    horizontal_pictures = []
    while pictures:
        if pictures[0].orientation == "V":
            vertical_pictures.append(pictures.pop(0))
        else:
            horizontal_pictures.append(pictures.pop(0))
    return vertical_pictures, horizontal_pictures
