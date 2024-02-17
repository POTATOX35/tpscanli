import requests
from discord import SyncWebhook 
import warnings
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from customtkinter import *
import os
import time
from PIL import Image, ImageFont, ImageDraw 
import packaging
import tkinter
import customtkinter
import locale
import json
from pynput.keyboard import Key, Listener
from plyer import notification






  
print("Takım 1 Oyuncu 1 tuşa basınız: ")
durum = "1"

def durum2():
    global durum
    print("Takım 1 Oyuncu 2 tuşa basınız: ")
    durum = "2"

def durum3():
    global durum
    print("Takım 1 Oyuncu 3 tuşa basınız: ")
    durum = "3"
def durum4():
    global durum
    print("Takım 2 Oyuncu 1 tuşa basınız: ")
    durum = "4"
def durum5():
    global durum
    print("Takım 2 Oyuncu 2 tuşa basınız: ")
    durum = "5"
def durum6():
    global durum
    print("Takım 2 Oyuncu 3 tuşa basınız: ")
    durum = "6"
def durum7():
    global durum
    print("Maçı bitirme tuşuna basınız: ")
    durum = "7"
def durum8():
    global durum
    print("Maçı başlatma tuşuna basınız: ")
    durum = "8"









def on_press(key):
    if durum == "1":
        
        
        f = open('settings.json', 'r',encoding="utf-8")
        
        data = json.load(f)
        data["key1"] = str(key) 
        f = open('settings.json', 'w',encoding="utf-8")
        json.dump(data, f)
        durum2()
    elif durum == "2":    
        f = open('settings.json', 'r',encoding="utf-8")
        
        data = json.load(f)
        data["key2"] = str(key) 
        f = open('settings.json', 'w',encoding="utf-8")
        json.dump(data, f)
        durum3()
    elif durum == "3":    
        f = open('settings.json', 'r',encoding="utf-8")
        
        data = json.load(f)
        data["key3"] = str(key) 
        f = open('settings.json', 'w',encoding="utf-8")
        json.dump(data, f)
        durum4()
    elif durum == "4":    
        f = open('settings.json', 'r',encoding="utf-8")
        
        data = json.load(f)
        data["key4"] = str(key) 
        f = open('settings.json', 'w',encoding="utf-8")
        json.dump(data, f)
        durum5()
    elif durum == "5":    
        f = open('settings.json', 'r',encoding="utf-8")
        
        data = json.load(f)
        data["key5"] = str(key) 
        f = open('settings.json', 'w',encoding="utf-8")
        json.dump(data, f)
        durum6()            
    elif durum == "6":    
        f = open('settings.json', 'r',encoding="utf-8")
        
        data = json.load(f)
        data["key6"] = str(key) 
        f = open('settings.json', 'w',encoding="utf-8")
        json.dump(data, f)
        durum7()
    elif durum == "7":    
        f = open('settings.json', 'r',encoding="utf-8")
        
        data = json.load(f)
        data["keyend"] = str(key) 
        f = open('settings.json', 'w',encoding="utf-8")
        json.dump(data, f) 
        durum8(123456)
    elif durum == "8":    
        f = open('settings.json', 'r',encoding="utf-8")
        
        data = json.load(f)
        data["keyhome"] = str(key) 
        f = open('settings.json', 'w',encoding="utf-8")
        json.dump(data, f)    
        
        
with Listener(on_press=on_press) as listener:

  
    #listener.stop()
   listener.join()




