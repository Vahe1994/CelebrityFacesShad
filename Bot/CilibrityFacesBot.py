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

def fill_storage():
    h = LSH(bits_number=10, embedding_dimention=128, hashtable_number=5)
    f = open('./mass_with_emb.txt')
    current_line = f.readline()
    while current_line:
        [name, vec] = current_line.split('\t')
        vec = list(map(float, vec[:-1].split(' ')))
        h.AddToStorages(vec, name)
        current_line = f.readline()
    return h

token = '595211498:AAFJzm4rtcJZrAOao-njv_jzrgntRb5V624'
bot = telebot.TeleBot(token)
Wheaherdict = []
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
lsh = fill_storage()
print('ready')

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

    image_content = misc.imread(f)
    photo = Facecrop.get_face(img= image_content) 
    photo =  Image.fromarray(photo)
    photo.save('lala.jpg')
   
    hashing = list(face_recognition.face_encodings(face_recognition.load_image_file('lala.jpg'))[0])
    
    nearest  = lsh.FindNSimilar(hashing,1)
    bot.send_message(message.chat.id,str(nearest[0][1]))


    bot.send_photo(message.chat.id,photo = open("img_align_celeba/"+nearest[0][1], 'rb'))


if __name__ == '__main__':
    
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except Exception as e:
            logger.error(e)
            time.sleep(3)
