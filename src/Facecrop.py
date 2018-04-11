import face_recognition
import scipy as sp
import scipy.misc
import matplotlib.pyplot as plt
import numpy as np
from imageio import imread

def get_face(img=None,url=None):
    face_locations=None
    if img is None:
        image = face_recognition.load_image_file("Jessica-Alba-Hot-photoshoot-2-834x1024.jpg")
        face_locations = face_recognition.face_locations(image)
    else:
        face_locations = face_recognition.face_locations(img)
    img =img[list(face_locations[0])[0]:list(face_locations[0])[2],list(face_locations[0])[3]:list(face_locations[0])[1]]
    return img