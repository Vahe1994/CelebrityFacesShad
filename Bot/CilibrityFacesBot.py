import telebot
import datetime
import random
import time
import logging
import os

import pandas as pd

import numpy as np
import sys
sys.path.insert(0, '../src/')
sys.path.insert(0, 'LSH/')
import Facecrop 
from PIL import Image
import io
from scipy import misc
import face_recognition
from LSH import LSH
import numpy as np
import os
import torch, torch.nn as nn
from torchvision import datasets, transforms
import torch.nn.functional as F
from torch.autograd import Variable




def fill_storage():
    h = LSH(bits_number=10, embedding_dimention=128, hashtable_number=5)
    f = open('./mass_with_emb_cropped.txt')
    current_line = f.readline()
    while current_line:
        [name, vec] = current_line.split('\t')
        vec = list(map(float, vec[:-1].split(' ')))
        h.AddToStorages(vec, name)
        current_line = f.readline()
    return h

<<<<<<< HEAD
class Flatten(nn.Module):
    def forward(self, input):
        return input.view(input.size(0), -1)

class VAE(nn.Module):
    def __init__(self, nc, ngf, ndf, latent_variable_size):
        super(VAE, self).__init__()

        self.nc = nc
        self.ngf = ngf
        self.ndf = ndf
        self.latent_variable_size = latent_variable_size

        # encoder
        self.e1 = nn.Conv2d(nc, ndf, 4, 2, 1)
        self.bn1 = nn.BatchNorm2d(ndf)

        self.e2 = nn.Conv2d(ndf, ndf*2, 4, 2, 1)
        self.bn2 = nn.BatchNorm2d(ndf*2)

        self.e3 = nn.Conv2d(ndf*2, ndf*4, 4, 2, 1)
        self.bn3 = nn.BatchNorm2d(ndf*4)

        self.e4 = nn.Conv2d(ndf*4, ndf*8, 4, 2, 1)
        self.bn4 = nn.BatchNorm2d(ndf*8)

        self.e5 = nn.Conv2d(ndf*8, ndf*8, 4, 2, 1)
        self.bn5 = nn.BatchNorm2d(ndf*8)

        self.fc1 = nn.Linear(ndf*8*4*4, latent_variable_size)
        self.fc2 = nn.Linear(ndf*8*4*4, latent_variable_size)

        # decoder
        self.d1 = nn.Linear(latent_variable_size, ngf*8*2*4*4)

        self.up1 = nn.UpsamplingNearest2d(scale_factor=2)
        self.pd1 = nn.ReplicationPad2d(1)
        self.d2 = nn.Conv2d(ngf*8*2, ngf*8, 3, 1)
        self.bn6 = nn.BatchNorm2d(ngf*8, 1.e-3)

        self.up2 = nn.UpsamplingNearest2d(scale_factor=2)
        self.pd2 = nn.ReplicationPad2d(1)
        self.d3 = nn.Conv2d(ngf*8, ngf*4, 3, 1)
        self.bn7 = nn.BatchNorm2d(ngf*4, 1.e-3)

        self.up3 = nn.UpsamplingNearest2d(scale_factor=2)
        self.pd3 = nn.ReplicationPad2d(1)
        self.d4 = nn.Conv2d(ngf*4, ngf*2, 3, 1)
        self.bn8 = nn.BatchNorm2d(ngf*2, 1.e-3)

        self.up4 = nn.UpsamplingNearest2d(scale_factor=2)
        self.pd4 = nn.ReplicationPad2d(1)
        self.d5 = nn.Conv2d(ngf*2, ngf, 3, 1)
        self.bn9 = nn.BatchNorm2d(ngf, 1.e-3)

        self.up5 = nn.UpsamplingNearest2d(scale_factor=2)
        self.pd5 = nn.ReplicationPad2d(1)
        self.d6 = nn.Conv2d(ngf, nc, 3, 1)

        self.leakyrelu = nn.LeakyReLU(0.2)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def encode(self, x):
        h1 = self.leakyrelu(self.bn1(self.e1(x)))
        h2 = self.leakyrelu(self.bn2(self.e2(h1)))
        h3 = self.leakyrelu(self.bn3(self.e3(h2)))
        h4 = self.leakyrelu(self.bn4(self.e4(h3)))
        h5 = self.leakyrelu(self.bn5(self.e5(h4)))
        h5 = h5.view(-1, self.ndf*8*4*4)

        return self.fc1(h5), self.fc2(h5)

    def reparametrize(self, mu, logvar):
        std = logvar.mul(0.5).exp_()
        if args.cuda:
            eps = torch.cuda.FloatTensor(std.size()).normal_()
        else:
            eps = torch.FloatTensor(std.size()).normal_()
        eps = Variable(eps)
        return eps.mul(std).add_(mu)

    def decode(self, z):
        h1 = self.relu(self.d1(z))
        h1 = h1.view(-1, self.ngf*8*2, 4, 4)
        h2 = self.leakyrelu(self.bn6(self.d2(self.pd1(self.up1(h1)))))
        h3 = self.leakyrelu(self.bn7(self.d3(self.pd2(self.up2(h2)))))
        h4 = self.leakyrelu(self.bn8(self.d4(self.pd3(self.up3(h3)))))
        h5 = self.leakyrelu(self.bn9(self.d5(self.pd4(self.up4(h4)))))

        return self.sigmoid(self.d6(self.pd5(self.up5(h5))))

    def get_latent_var(self, x):
        mu, logvar = self.encode(x.view(-1, self.nc, self.ndf, self.ngf))
        z = self.reparametrize(mu, logvar)
        return z

    def forward(self, x):
        mu, logvar = self.encode(x.view(-1, self.nc, self.ndf, self.ngf))
        z = self.reparametrize(mu, logvar)
        res = self.decode(z)
        return res, mu, logvar



token = '595211498:AAFJzm4rtcJZrAOao-njv_jzrgntRb5V624'
=======
token = ''
>>>>>>> 5c15d5ee6bae223df7463f44a2c47f40e5eda98f
bot = telebot.TeleBot(token)
Wheaherdict = []
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
lsh = fill_storage()
totensor = transforms.ToTensor()
model = torch.load('model', map_location={'cuda:0': 'cpu'})
print('ready')

def get_average(nearest):
    img = Image.open('lala.jpg')
    img = img.resize((128,128))
    enc = model.encode(Variable(totensor(img).unsqueeze(0)))[0]
    try:
        img = Facecrop.get_face(img= None,url="face_image/"+nearest)
    except:
        img = Facecrop.get_face(img= None,url="img_align_celeba/"+nearest) 
        print(2)

    img =  Image.fromarray(img)
    
    img = img.resize((128,128))
    enc = (enc+model.encode(Variable(totensor(img).unsqueeze(0)))[0])/2.0
    dec = model.decode(enc)
    return np.swapaxes(np.swapaxes(dec[0].data.numpy(),0,2),0,1)

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id,
                     "Make a look what cilibrity look alike you! For help type /help")


@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id,
                     'To start using this program just upload your photo. ')
    bot.send_message(message.chat.id,
                     'For any bug report you can send report to vahe527887@yandex.ru  or aizakharov94@gmail.com .\n Thank you for support.Good Hunt and have fun! ;)')


@bot.message_handler(content_types=["text"])
def just_do_t(message):
    bot.send_message(message.chat.id,
                             "Your request is not valid.Please upload photo not text.")

@bot.message_handler(content_types=["photo"])
def just_do_photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    f = io.BytesIO(downloaded_file)
    try:
        image_content = misc.imread(f)
        photo = Facecrop.get_face(img= image_content) 
        photo =  Image.fromarray(photo)
        photo.save('lala.jpg')

        hashing = list(face_recognition.face_encodings(face_recognition.load_image_file('lala.jpg'))[0])
        
        nearest  = lsh.FindNSimilar(hashing,1)
        
        bot.send_message(message.chat.id,"Here is a Celebrity that look like you .")
        bot.send_photo(message.chat.id,photo = open("img_align_celeba/"+nearest[0][1], 'rb'))
        photo = get_average(nearest[0][1])
        
        misc.imsave('lala.jpg',photo)
        bot.send_message(message.chat.id,"And a mix of you and that Celebrity .")
        bot.send_photo(message.chat.id,photo = open("lala.jpg", 'rb'))
    except:
        bot.send_message(message.chat.id,"In this photo there is no face detected :( Please try another one.")



if __name__ == '__main__':
    
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            logger.error(e) 
            time.sleep(3)
