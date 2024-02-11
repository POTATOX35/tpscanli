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



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


if locale.getdefaultlocale()[0] == "tr_TR":
    dil = "tr_TR"
elif locale.getdefaultlocale()[0] == "en_EN":
    dil = "en_EN"



with open('settings.json', 'r',encoding="utf-8") as f:
  data = json.load(f)
  echeck = data["Everyonecheck"]
  
if str(echeck) == "True":
      everyonecheck = "@everyone"
else:
      everyonecheck = "" 
  
if data["Lang"] == locale.getdefaultlocale()[0]:
    pass
else:
    data["Lang"] = str(dil) 
    


with open('settings.json', 'w',encoding="utf-8") as f:
    json.dump(data, f)


with open('settings.json', 'r',encoding="utf-8") as f:
  data = json.load(f)
  url = data['URL']
  language = str(data["Lang"])

with open(language+'.json', 'r',encoding="utf-8") as f:
  lang = json.load(f)
  



rot = customtkinter.CTk()
rot.geometry("400x475")
rot.title(str(lang["Title"]))

rot.resizable(0,0)
skor = 0
skors = 0

golbir1 =0
golbir2 =0
golbir3 = 0

goliki1 =0
goliki2 =0
goliki3 = 0
webhook = SyncWebhook.from_url(str(url)) 
def goltakımbir1():
    global skor
    global skors
    global golbir1
    golbir1 +=1
    skor += 1
    
    message = str(lang["Goal"]) + str(takimadibir.get()) + str(lang["Found"]) + str(oyuncuaditakimbir1.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ everyonecheck
    webhook.send(str(message))
def goltakımbir2():
    global skor
    global skors
    global golbir2
    golbir2 +=1
    skor += 1
    message = str(lang["Goal"]) + str(takimadibir.get()) + str(lang["Found"]) + str(oyuncuaditakimbir2.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ everyonecheck
    webhook.send(str(message))
def goltakımbir3():
    global skor
    global skors
    global golbir3
    golbir3 +=1
    skor += 1
    message = str(lang["Goal"]) + str(takimadibir.get()) + str(lang["Found"]) + str(oyuncuaditakimbir3.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ everyonecheck
    webhook.send(str(message))        
def goltakımiki1():
    global skor
    global skors
    global goliki1
    goliki1 +=1
    skors += 1
    message = str(lang["Goal"]) + str(takimadiiki.get()) + str(lang["Found"]) + str(oyuncuaditakimiki1.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ everyonecheck
    webhook.send(str(message))
def goltakımiki2():
    global skor
    global skors
    global goliki2
    goliki2 +=1
    skors += 1
    message = str(lang["Goal"]) + str(takimadiiki.get()) + str(lang["Found"]) + str(oyuncuaditakimiki2.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ everyonecheck
    webhook.send(str(message))
def goltakımiki3():
    global skor
    global skors
    global goliki3
    goliki3 +=1
    skors += 1
    message = str(lang["Goal"]) + str(takimadiiki.get()) + str(lang["Found"]) + str(oyuncuaditakimiki3.get()) + " !!!" + "\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get())+ everyonecheck
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
    message = "Maç başladı !!!" +"\n"+str(takimadibir.get())+" " +"-" + " "+ str(takimadiiki.get())+everyonecheck
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
    message = "Maç sona erdi !!!" +"\n"+str(takimadibir.get())+" " + str(skor)+" " + "-" + " "+str(skors) +" " + str(takimadiiki.get()) 
    message += str(lang["Most"])
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
    message+=" \n"+everyonecheck            
    webhook.send(str(message))
    
fontssss = customtkinter.CTkFont(family='fontui.ttf', size=16)









frame = customtkinter.CTkFrame(master=rot)
frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

frames = customtkinter.CTkFrame(master=rot)
frames.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")




label = customtkinter.CTkLabel(master=frame, text=str(lang["Label1"]),font=fontssss)
label.pack(pady=12,padx=10)

labels = customtkinter.CTkLabel(master=frames, text=str(lang["Label2"]),font=fontssss)
labels.pack(pady=12,padx=10)

takimadibir = customtkinter.CTkEntry(master=frame,placeholder_text=str(lang["Teamname"]),font=fontssss)
takimadibir.pack(pady=12,padx=10) 
takimadiiki= customtkinter.CTkEntry(master=frames,placeholder_text=str(lang["Teamname"]),font=fontssss)
takimadiiki.pack(pady=12,padx=10) 

oyuncuaditakimbir1 = customtkinter.CTkEntry(master=frame,placeholder_text=str(lang["Firstpl"]),font=fontssss)
oyuncuaditakimbir1.pack(pady=12,padx=10) 
oyuncuaditakimiki1 = customtkinter.CTkEntry(master=frames,placeholder_text=str(lang["Firstpl"]),font=fontssss)
oyuncuaditakimiki1.pack(pady=12,padx=10) 
oyuncuaditakimbir2 = customtkinter.CTkEntry(master=frame,placeholder_text=str(lang["Secondpl"]),font=fontssss)
oyuncuaditakimbir2.pack(pady=12,padx=10) 
oyuncuaditakimiki2 = customtkinter.CTkEntry(master=frames,placeholder_text=str(lang["Secondpl"]),font=fontssss)
oyuncuaditakimiki2.pack(pady=12,padx=10) 
oyuncuaditakimbir3 = customtkinter.CTkEntry(master=frame,placeholder_text=str(lang["Thirdpl"]),font=fontssss)
oyuncuaditakimbir3.pack(pady=12,padx=10) 
oyuncuaditakimiki3 = customtkinter.CTkEntry(master=frames,placeholder_text=str(lang["Thirdpl"]),font=fontssss)
oyuncuaditakimiki3.pack(pady=12,padx=10) 


button = customtkinter.CTkButton(master=frame, text=str(lang["Goal1"]), command=goltakımbir1,font=fontssss)
button.pack(pady=12,padx=10)
buttosn = customtkinter.CTkButton(master=frames, text=str(lang["Goal1"]), command=goltakımiki1,font=fontssss)
buttosn.pack(pady=12,padx=10)
button = customtkinter.CTkButton(master=frame, text=str(lang["Goal2"]), command=goltakımbir2,font=fontssss)
button.pack(pady=12,padx=10)
buttosnn = customtkinter.CTkButton(master=frames, text=str(lang["Goal2"]), command=goltakımiki2,font=fontssss)
buttosnn.pack(pady=12,padx=10)
button = customtkinter.CTkButton(master=frame, text=str(lang["Goal3"]), command=goltakımbir3,font=fontssss)
button.pack(pady=12,padx=10)
buttosnnn = customtkinter.CTkButton(master=frames, text=str(lang["Goal3"]), command=goltakımiki3,font=fontssss)
buttosnnn.pack(pady=12,padx=10)
bitir = customtkinter.CTkButton(master=frame, text=str(lang["End"]), command=bitirs,font=fontssss)
bitir.pack(pady=12,padx=10)
baslat = customtkinter.CTkButton(master=frames, text=str(lang["Start"]), command=baslats,font=fontssss)
baslat.pack(pady=12,padx=10)



rot.mainloop()
