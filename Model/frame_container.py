
import matplotlib._png as png


class FrameContainer(object):
    def __init__(self, img_path):
        self.img = png.read_png_int(img_path)
        self.traffic_light = []
        self.traffic_lights_3d_location = []
        self.EM = []
        self.corresponding_ind = []
        self.valid = []
