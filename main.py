from input_parser import read_file
from collection import Collection
from slideshow import Slideshow
from Process import get_slideshow

filename = "a_example.txt"


def main():
    collection = Collection()
    read_file(filename, collection)

    slideshow = get_slideshow(collection.get_array())

    slideshow.parse_output()

    print("Done")


if __name__ == "__main__":
    main()