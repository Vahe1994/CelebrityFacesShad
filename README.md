# CilibrityFaceShad

## Dependencies
* Python 3 with numpy,face_recognition
* Tensorflow (1.0+), we recomended to use r1.7


First you must download pretrained model from  https://github.com/davidsandberg/facenet ( Pre-trained models)
Datasets you can find here http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html


### Face detection and cropping 
 As it mention in https://github.com/davidsandberg/facenet ,  best result the best way to detect face we can approach by using MTCNN ,we do it with 
https://pypi.python.org/pypi/face_recognition,which built using dlib’s state-of-the-art face recognition built with deep learning. 

