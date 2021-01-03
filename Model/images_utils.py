
import numpy as np


def pad_image(img):
    height, width, _ = img.shape
    padded_img = np.zeros((height + 81, width + 81, 3), dtype='uint8')
    padded_img[40:height + 40, 40:width + 40, :] = img
    return padded_img


def crop(img, y, x):
    padded_img = pad_image(img)
    return padded_img[x:x + 81, y:y + 81, :]


def crop_image(img, cand_list):
    cropped = [crop(img, i[0], i[1]) for i in cand_list]
    return [x for x in cropped if x.shape == (81, 81, 3)]

