from input_parser import read_file
from collection import Collection
from slideshow import Slideshow
from photo import Photo
from slide import Slide

filename = "a_example.txt"


def main():
    collection = Collection()
    slideshow = Slideshow()
    read_file(filename, collection)

    slideshow.parse_output()

    print("Done")


if __name__ == "__main__":
    main()