from input_parser import read_file
from collection import Collection
from slideshow import Slideshow
from Process import get_slideshow

input_folder = "inputfiles"
output_folder = "outputfiles"
filename = "e_shiny_selfies.txt"


def main():
    collection = Collection()
    read_file(input_folder + "/" + filename, collection)

    slideshow = get_slideshow(collection.get_array())

    slideshow.parse_output(output_folder + "/" + filename)

    print("Done")


if __name__ == "__main__":
    main()