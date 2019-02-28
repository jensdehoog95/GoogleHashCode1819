from slide import Slide
from photo import Photo


def preprocess_pictures(pictures):
    vertical_pictures = remove_vertical_pictures(pictures)
    horizontal_pictures= pictures
    merged_slides = merge_vertical_pictures(vertical_pictures)
    slides = []
    slides.extend(merged_slides)
    for picture in horizontal_pictures:
        slides.append(Slide(picture))
    return pictures


def merge_vertical_pictures(vertical_pictures):
    pictures = sort_pictures(vertical_pictures)
    merged_pictures = []
    while len(pictures) > 1:
        v1 = pictures.pop([0])
        v2 = pictures.pop([-1])

        slide = Slide(v1, v2)
        merged_pictures.append(slide)
    return merged_pictures


def sort_pictures(vertical_pictures):
    sorted_pictures = vertical_pictures.sort(key=lambda x: x.tags.count, reverse=True)
    return sorted_pictures


def remove_vertical_pictures(pictures):
    vertical_pictures = []
    for i in range(len(pictures)):
        if pictures[i].orientation == "V":
            vertical_pictures.append(pictures.pop(i))
    return vertical_pictures
