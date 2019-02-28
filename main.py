from input_parser import read_file
from collection import Collection
from slideshow import Slideshow
from Process import get_slideshow

input_folder = "inputfiles"
output_folder = "outputfiles"
filename = "a_example.txt"


def main():
    collection = Collection()
    read_file(input_folder + "/" + filename, collection)
    searchlength = 100
    difference = 3
    sort = 0
    merge_type = 0
    slideshow = get_slideshow(collection.get_array(),searchlength,difference,sort, merge_type)
    print(slideshow.score())

    slideshow.parse_output(output_folder + "/" + filename)

    print("Done")


if __name__ == "__main__":
    main()