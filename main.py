from imports import *
from _3_soru_yarat import soru_yarat
from _4_userlogin import userLogin
from _5_yarisma import game
from _6_soru_gonder import oyunbitir

username = "efe@sd.com"
password = "abc"

if userLogin(password,username):
    sorular = soru_yarat()
    score = game(sorular)
    bitir = oyunbitir(username,score,sorular)
    if bitir:
        print("oyun kaydedildi.")
    