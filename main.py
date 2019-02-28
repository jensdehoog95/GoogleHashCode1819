from input_parser import read_file
from collection import Collection
from slideshow import Slideshow
from Process import get_slideshow

filename = "inputfiles/a_example.txt"


def main():
    collection = Collection()
    read_file(filename, collection)
    searchlength = 100
    difference = 3
    sort = 0
    slideshow = get_slideshow(collection.get_array(),searchlength,difference,sort)
    print(slideshow.score())

    slideshow.parse_output()

    print("Done")


if __name__ == "__main__":
    main()