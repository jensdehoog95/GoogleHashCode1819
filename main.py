from input_parser import read_file
from collection import Collection
from slideshow import Slideshow
from Process import get_slideshow
import sys

input_folder = "inputfiles"
output_folder = "outputfiles"
filename = "d_pet_pictures.txt"


def main():
    global filename
    input=input_folder+"/"+filename;
    if len(sys.argv)>1 and sys.argv[1] is not None:
        input = sys.argv[1]
    collection = Collection()
    read_file(input, collection)
    best_searchlength = 100
    best_difference = 3
    best_sort = 0
    best_merge_type = 0
    best_score = 0
    for searchlength in range(10, 500):
        for difference in range(0, 30):
            for sort in range(0, 3):
                for merge_type in range(0,2):
                    try:
                        slideshow = get_slideshow(collection.get_array().copy(),searchlength,difference,sort, merge_type)
                    except:
                       continue

                    score = slideshow.score()
                    if(score>best_score):
                        best_searchlength=searchlength
                        best_difference=difference
                        best_sort= sort
                        best_merge_type=merge_type
    print("search length" + str(best_searchlength))
    print("diff"+str(best_difference))
    print("sort"+str(best_sort))
    print("merge_type"+str(best_merge_type))

    print(slideshow.score())

    slideshow.parse_output(output_folder + "/" + filename)

    print("Done")


if __name__ == "__main__":
    main()