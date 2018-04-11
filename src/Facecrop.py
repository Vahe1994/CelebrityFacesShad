import face_recognition
import matplotlib.pyplot as plt
import numpy as np
from imageio import imread

def get_face(img=None,url=None):
    face_locations=None
    if img is None:
        img = face_recognition.load_image_file(url)
        face_locations = face_recognition.face_locations(img)
    else:
        face_locations = face_recognition.face_locations(img)
    img =img[list(face_locations[0])[0]:list(face_locations[0])[2],list(face_locations[0])[3]:list(face_locations[0])[1]]
    return img