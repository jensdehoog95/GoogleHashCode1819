from collection import Collection

def read_file(file, collection: Collection):
    with open(file) as f:
        line = f.readline()