from utils import *
import cv2
import numpy
from datetime import datetime, timedelta


def get_black_background():
    return numpy.zeros((300, 300, 3))


start_time = datetime(2019, 1, 1)
end_time = start_time + timedelta(days=1)


def generate_image_with_text(text):
    image = get_black_background()
    font = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(image, text, (60, 170), font, 2, (0, 150, 0), 1)
    return image


while start_time < end_time:
    text = convert_time_to_string(start_time)
    image = generate_image_with_text(text)
    cv2.imwrite('time_images/{text}.jpeg'.format(text=text), image)
    start_time += timedelta(minutes=1)
