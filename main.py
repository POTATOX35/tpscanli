import requests
from discord import SyncWebhook # Import SyncWebhook
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




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")







rot = customtkinter.CTk()
rot.geometry("400x475")
rot.title("TPS Canlı Skor Panel")

rot.resizable(0,0)
skor = 0
skors = 0

golbir1 =0
golbir2 =0
golbir3 = 0

goliki1 =0
goliki2 =0
goliki3 = 0
webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/1205926575908982855/YefibiS5v8oJJthp05l5f-sCN1cGVnR1VWdH3ImHwjrAoeYnKg_T9vyAY0R3CQLbMPqT') # Initializing webhook
def goltakımbir1():
    global skor
    global skors
    global golbir1
    golbir1 +=1
    skor += 1
    
    message = "GOOOL !!! " + str(takimadibir.get()) + " golü buldu ! Golün adı: " + str(oyuncuaditakimbir1.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ " @everyone"
    webhook.send(str(message))
def goltakımbir2():
    global skor
    global skors
    global golbir2
    golbir2 +=1
    skor += 1
    message = "GOOOL !!! " + str(takimadibir.get()) + " golü buldu ! Golün adı: " + str(oyuncuaditakimbir2.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ " @everyone"
    webhook.send(str(message))
def goltakımbir3():
    global skor
    global skors
    global golbir3
    golbir3 +=1
    skor += 1
    message = "GOOOL !!! " + str(takimadibir.get()) + " golü buldu ! Golün adı: " + str(oyuncuaditakimbir3.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ " @everyone"
    webhook.send(str(message))        
def goltakımiki1():
    global skor
    global skors
    global goliki1
    goliki1 +=1
    skors += 1
    message = "GOOOL !!! " + str(takimadiiki.get()) + " golü buldu ! Golün adı: " + str(oyuncuaditakimiki1.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ " @everyone"
    webhook.send(str(message))
def goltakımiki2():
    global skor
    global skors
    global goliki2
    goliki2 +=1
    skors += 1
    message = "GOOOL !!! " + str(takimadiiki.get()) + " golü buldu ! Golün adı: " + str(oyuncuaditakimiki2.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ " @everyone"
    webhook.send(str(message))
def goltakımiki3():
    global skor
    global skors
    global goliki3
    goliki3 +=1
    skors += 1
    message = "GOOOL !!! " + str(takimadiiki.get()) + " golü buldu ! Golün adı: " + str(oyuncuaditakimiki3.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ " @everyone"
    webhook.send(str(message))        
def baslats():
    global skor
    global skors
    global golbir1
    global golbir2
    global golbir3
    global goliki1
    global goliki2
    global goliki3
    skors =0
    skor =0
    golbir1 =0
    golbir2 =0
    golbir3 = 0

    goliki1 =0
    goliki2 =0
    goliki3 = 0
    message = "Maç başladı !!!" +"\n"+str(takimadibir.get())+" " +"-" + " "+ str(takimadiiki.get())+" @everyone"
    webhook.send(str(message))
def bitirs():
    global skor
    global skors
    global golbir1
    global golbir2
    global golbir3
    global goliki1
    global goliki2
    global goliki3
    global oyuncuaditakimbir1
    message = "Maç sona erdi !!!" +"\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get()) 
    message += "\n"
    var = {golbir1:oyuncuaditakimbir1.get(),golbir2:oyuncuaditakimbir2.get(),golbir3:oyuncuaditakimbir3.get(),goliki1:oyuncuaditakimiki1.get(),goliki2:oyuncuaditakimiki2.get(),goliki3:oyuncuaditakimiki3.get(),}
    
    if golbir1 > 0:
        message += "\n" +oyuncuaditakimbir1.get() + ": "+ golbir1*(":soccer:")
    if golbir2 > 0:
        message += "\n" +oyuncuaditakimbir2.get() + ": "+ golbir2*(":soccer:")
    if golbir3 > 0:
        message += "\n" +oyuncuaditakimbir3.get() + ": "+ golbir3*(":soccer:")
    if goliki1 > 0:
        message += "\n" +oyuncuaditakimiki1.get() + ": "+ goliki1*(":soccer:")
    if goliki2 > 0:
        message += "\n" +oyuncuaditakimiki2.get() + ": "+ goliki2*(":soccer:")
    if goliki3 > 0:
        message += "\n" +oyuncuaditakimiki3.get() + ": "+ goliki3*(":soccer:")    
    
    
    message+= "\nEn golcü: "+ str(var.get(max(golbir1,golbir2,golbir3,goliki1,goliki2,goliki3)))
    message+=" \n@everyone"            
    webhook.send(str(message))
    
fontssss = customtkinter.CTkFont(family='fontui.ttf', size=16)









frame = customtkinter.CTkFrame(master=rot)
frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

frames = customtkinter.CTkFrame(master=rot)
frames.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

# Show image using label 


label = customtkinter.CTkLabel(master=frame, text="Takım 1",font=fontssss)
label.pack(pady=12,padx=10)

labels = customtkinter.CTkLabel(master=frames, text="Takım 2",font=fontssss)
labels.pack(pady=12,padx=10)

takimadibir = customtkinter.CTkEntry(master=frame,placeholder_text="Takım Adı",font=fontssss)
takimadibir.pack(pady=12,padx=10) 
takimadiiki= customtkinter.CTkEntry(master=frames,placeholder_text="Takım Adı",font=fontssss)
takimadiiki.pack(pady=12,padx=10) 

oyuncuaditakimbir1 = customtkinter.CTkEntry(master=frame,placeholder_text="1. Oyuncu",font=fontssss)
oyuncuaditakimbir1.pack(pady=12,padx=10) 
oyuncuaditakimiki1 = customtkinter.CTkEntry(master=frames,placeholder_text="1. Oyuncu",font=fontssss)
oyuncuaditakimiki1.pack(pady=12,padx=10) 
oyuncuaditakimbir2 = customtkinter.CTkEntry(master=frame,placeholder_text="2. Oyuncu",font=fontssss)
oyuncuaditakimbir2.pack(pady=12,padx=10) 
oyuncuaditakimiki2 = customtkinter.CTkEntry(master=frames,placeholder_text="2. Oyuncu",font=fontssss)
oyuncuaditakimiki2.pack(pady=12,padx=10) 
oyuncuaditakimbir3 = customtkinter.CTkEntry(master=frame,placeholder_text="3. Oyuncu",font=fontssss)
oyuncuaditakimbir3.pack(pady=12,padx=10) 
oyuncuaditakimiki3 = customtkinter.CTkEntry(master=frames,placeholder_text="3. Oyuncu",font=fontssss)
oyuncuaditakimiki3.pack(pady=12,padx=10) 


button = customtkinter.CTkButton(master=frame, text="Gol 1", command=goltakımbir1,font=fontssss)
button.pack(pady=12,padx=10)
buttosn = customtkinter.CTkButton(master=frames, text="Gol 1", command=goltakımiki1,font=fontssss)
buttosn.pack(pady=12,padx=10)
button = customtkinter.CTkButton(master=frame, text="Gol 2", command=goltakımbir2,font=fontssss)
button.pack(pady=12,padx=10)
buttosnn = customtkinter.CTkButton(master=frames, text="Gol 2", command=goltakımiki2,font=fontssss)
buttosnn.pack(pady=12,padx=10)
button = customtkinter.CTkButton(master=frame, text="Gol 3", command=goltakımbir3,font=fontssss)
button.pack(pady=12,padx=10)
buttosnnn = customtkinter.CTkButton(master=frames, text="Gol 3", command=goltakımiki3,font=fontssss)
buttosnnn.pack(pady=12,padx=10)
bitir = customtkinter.CTkButton(master=frame, text="Maçı Bitir", command=bitirs,font=fontssss)
bitir.pack(pady=12,padx=10)
baslat = customtkinter.CTkButton(master=frames, text="Maçı Başlat", command=baslats,font=fontssss)
baslat.pack(pady=12,padx=10)



rot.mainloop()
