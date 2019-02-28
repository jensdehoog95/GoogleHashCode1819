from photo import Photo

class Collection():
    def __init__(self):
        self.photos = []

    def add_photo(self, photo: Photo):
        self.photos.append(photo)

    def get_array(self):
        return self.photos
