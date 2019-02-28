from input_parser import read_file
from collection import Collection
from slideshow import Slideshow
from Process import get_slideshow
from threading import Thread

input_folder = "inputfiles"
output_folder = "outputfiles"
filename = "a_example.txt"


def main():
    collection = Collection()
    read_file(input_folder + "/" + filename, collection)

    tuples = []
    threads = []

    for difference in range(0, 30):
        # difference_function(collection, tuples, difference)
        thread = Thread(target=difference_function, args=(collection.get_array().copy(), tuples, difference,))
        threads.append(thread)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    best_tuple = get_best_tuple(tuples)
    print_tuple(best_tuple)

    slideshow = get_slideshow(collection.get_array().copy(),
                              best_tuple[1], best_tuple[2], best_tuple[3],
                              best_tuple[4])

    print(slideshow.score())

    slideshow.parse_output(output_folder + "/" + filename)

    print("Done")


def difference_function(collection, tuples, difference):
    best_searchlength = 100
    best_difference = 3
    best_sort = 0
    best_merge_type = 0
    best_score = 0

    best_tuple = ()

    for searchlength in range(10, 500):
        for sort in range(0, 3):
            for merge_type in range(0, 2):
                try:
                    slideshow = get_slideshow(collection,
                                              searchlength, difference, sort,
                                              merge_type)
                except:
                    continue

                score = slideshow.score()
                if (score > best_score):
                    best_searchlength = searchlength
                    best_difference = difference
                    best_sort = sort
                    best_merge_type = merge_type
                    best_score = score

                    best_tuple = (
                        best_score, best_searchlength,
                        best_difference, best_sort,
                        best_merge_type)

    tuples.append(best_tuple)
    return best_tuple


def get_best_tuple(tuples):
    best_score = 0
    best_tuple = ()
    for t in tuples:
        if t[0] > best_score:
            best_score = t[0]
            best_tuple = t

    return best_tuple


def print_tuple(tuple):
    print("Best score: " + str(tuple[0]))
    print("search length: " + str(tuple[1]))
    print("diff: " + str(tuple[2]))
    print("sort: " + str(tuple[3]))
    print("merge_type: " + str(tuple[4]))


if __name__ == "__main__":
    main()