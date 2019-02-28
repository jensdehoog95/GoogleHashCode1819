from photo import Photo

class Slide():
    def __init__(self, photo1: Photo=None, photo2: Photo=None):
        self.photo1 = photo1
        self.photo2 = photo2

    def get_tags(self):
        tags=[]
        tags.extend(self.photo1.tags)
        tags.extend(self.photo2.tags)
        return tags

