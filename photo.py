from tag import Tag

class Photo():
    def __init__(self, idx, tags, orientation):
        self.idx = idx
        self.tags = tags
        self.orientation = orientation

    def add_tag(self, tag):
        self.tags.append(tag)
