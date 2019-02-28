from photo import Photo

class Slide():
    def __init__(self, photo1=None, photo2=None):
        self.photo1 = photo1
        self.photo2 = photo2

        self.tags=[]

        if photo1 is not None:
            self.tags.extend(self.photo1.tags)

        if photo2 is not None:
            self.tags.extend(self.photo2.tags)

