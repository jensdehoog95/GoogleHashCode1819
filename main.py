from input_parser import read_file
from collection import Collection

filename = "a_example.txt"


def main():
    collection = Collection()
    read_file(filename, collection)
    print("Done")


if __name__ == "__main__":
    main()