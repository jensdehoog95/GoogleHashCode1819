from slide import Slide

output_file = "output.txt"


class Slideshow():
    def __init__(self):
        self.slides = []

    def add_slide(self, slide: Slide):
        self.slides.append(slide)

    def parse_output(self, filename):
        with open(filename, "w") as f:
            num_slides = self._get_num_slides()
            self._write_line(f, str(num_slides) + '\n')

            for x in range(len(self.slides)):
                slide = self.slides[x]

                tmp_photo = slide.photo1
                if tmp_photo is not None:
                    self._write_line(f, str(tmp_photo.idx))
                else:
                    raise ValueError('Photo 1 in slide does not exist')

                tmp_photo = slide.photo2
                if tmp_photo is not None:
                    self._write_line(f, ' ' + str(tmp_photo.idx))

                self._write_line(f, '\n')

    def _get_num_slides(self):
        return len(self.slides)

    def _write_line(self, file, line):
        file.write(line)
