from collection import Collection
from tag import Tag
from photo import Photo


def read_file(file, collection: Collection):
    with open(file) as f:
        header = f.readline()
        num_photos = _parse_header(header)

        for x in range(num_photos):
            line = f.readline()
            photo = _parse_photo(x, line)
            collection.add_photo(photo)


def _parse_header(header):
    return int(header)


def _parse_photo(idx, line):
    splitline = line.split()
    orientation = splitline[0]
    num_tags = int(splitline[1])
    tags =[]
    for y in range(num_tags):
        tag = Tag(splitline[2 + y]) # Index of tags in splitline starts at 2
        tags.append(tag)

    photo = Photo(idx, tags, orientation)
    return photo


