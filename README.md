# CelebrityFaceSDA

In this git repository, we are providing code that we are using in our version of Celebrity Faces.
You can try how well this is working in or site URL.


## Dependencies
* Python 3 with numpy,face_recognition
* Tensorflow (1.0+), we recomended to use r1.7


First, you must download the pre-trained model from  https://github.com/davidsandberg/facenet ( Pre-trained models)
Datasets you can find here http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html

### Done
 * We have done required module (3 points)
 * Was realized good approximate method (3 people 0.5 points)
 * Our own neural network to get embeddings (1 point)
 * Was realized method which generates face which is similar to yours and Celebrity you look like. (0.7 points)

### Face detection and cropping 
 As it mentioned in https://github.com/davidsandberg/facenet ,  best result the best way to detect face we can approach by using MTCNN , we do it with 
https://pypi.python.org/pypi/face_recognition (built using dlib’s state-of-the-art face recognition) deep learning library.
 In the future, we will try also MTCNN.

### Index
 Index was written using Locality-Sensitive Hashing algorithm. We use 10 bits for hashing embeddings. We use 5 hash tables. Index was realized using compiling language C++ and was connected to Telegram Bot using Cython.

### Our NN
 * To get embeddings we use VAE with BCE + KDE losses.
 * To generate face which is similar to yours and Celebrity one we decode mean value between two these two faces embeddings.

![alt text](http://www.speedupcode.com/wp-content/uploads/2018/02/scheme_little_color.png)