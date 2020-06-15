#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:40:32 2020

@author: nur
"""


# --------------- IMPORT ALL MODULES ------------------------------------------

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

# --------------- USER INTERFACE ----------------------------------------------

root = tk.Tk()
root.title( "Yüksek Öğrenim Sıralama    " )

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 720
window_height = 550

window_position_x = 0
window_position_y = 0
root.geometry("310x300")

frame = tk.Frame(root, bg='cyan')
frame.pack(side="bottom", fill='both', expand='no')



konumPuanıLabel = Label(root,width=20,height=3,text="KONUM PUANI" , font="Times 10 bold")
konumPuanıLabel.place(x=30 ,y=26)

akademikYayinSayisiLabel = Label(root,width=20,height=3,text="YAYIN SAYISI" , font="Times 10 bold")
akademikYayinSayisiLabel.place(x=30,y=66)

yayinDerecesiLabel = Label(root,width=20,height=3,text="YAYIN DERECESİ" , font="Times 10 bold")
yayinDerecesiLabel.place(x=30 ,y=106)

ogrenciSeviyesiLabel = Label(root,width=20,height=3,text="ÖĞRENCİ SEVİYESİ" , font="Times 10 bold")
ogrenciSeviyesiLabel.place(x=30,y=146)

dersSaatiLabel = Label(root,width=20,height=3,text="DERS SAATİ " , font="Times 10 bold")
dersSaatiLabel.place(x=30 ,y=186)



konumPuanı_edit = Entry(root,width=5)
konumPuanı_edit.place(x=200,y=40)
konumPuanı_edit.config(font="bold")
konumPuanı_edit.insert(END,"")

akademikYayinSayisi_edit = Entry(root,width=5)
akademikYayinSayisi_edit.place(x=200,y=80)
akademikYayinSayisi_edit.config(font="bold")
akademikYayinSayisi_edit.insert(END,"")

yayinDerecesi_edit = Entry(root,width=5)
yayinDerecesi_edit.place(x=200,y=120)
yayinDerecesi_edit.config(font="bold")
yayinDerecesi_edit.insert(END,"")

ogrenciSeviyesi_edit = Entry(root,width=5)
ogrenciSeviyesi_edit.place(x=200,y=160)
ogrenciSeviyesi_edit.config(font="bold")
ogrenciSeviyesi_edit.insert(END,"")

dersSaati_edit = Entry(root,width=5)
dersSaati_edit.place(x=200,y=200)
dersSaati_edit.config(font="bold")
dersSaati_edit.insert(END,"")


# ------------------- MAIN FUNCTION -------------------------------------------

def Calculate():

    # --------------- GET USER'S DATA FROM INTERFACE --------------------------

    konumPuanı = int(konumPuanı_edit.get())
    yayinSayisi = int(akademikYayinSayisi_edit.get())
    yayinDerecesi = int(yayinDerecesi_edit.get())
    ogrenciSeviyesi = int(ogrenciSeviyesi_edit.get())
    dersSaati = int(dersSaati_edit.get())
    
    # --------------- GET MAIN DATA FROM CSV FILE -----------------------------

    
    
    mainData = pd.read_csv("data.csv")
    mainData.isnull().sum()
    #mainData = mainData.dropna() 
    mainData.drop(['BoşSütun1', 'BoşSütun2'], axis =1, inplace = True) 
    
    from sklearn.impute import SimpleImputer
    
    imputer = SimpleImputer(missing_values = np.NaN, strategy = 'mean', fill_value=None, verbose=0)
    Data = mainData.iloc[:,0:5].values
    print(Data)
    
    imputer = imputer.fit(Data[:,0:5])
    Data[:,0:5] = imputer.transform(Data[:,0:5])
    print(Data)
    
# --------------- MENTION FEATURES AND RESULT ATTRIBUTE -------------------
        
    
    features = Data[:,0:5]
    features = pd.DataFrame(data = features, index = range(19), columns=['Konum','AkademikYayinSayisi','AkademikYayinDerecesi','OgrenciSeviyesi','DersSaati'])
    print(features) # burayi kaldirabilirsin
    
    resultAttribute = mainData.sr

    # --------------- CALL NAIVE BAYES ---------------------------------------

    reg = GaussianNB()
    

    # --------------- FITTING OPERATION WITH FEATURES AND RESULT ATTRIBUTE ----

    reg.fit(features, resultAttribute)

    # --------------- PREDICT OPERATION ---------------------------------------

    testAttributes = [[konumPuanı, yayinSayisi, yayinDerecesi, ogrenciSeviyesi, dersSaati]]
    predictResult = reg.predict(testAttributes)
    lastResult = int(predictResult)

    # --------------- SHOW RESULT ---------------------------------------------

    tk.messagebox.showinfo("\n TAHMİNİ SIRA" , lastResult)

    # --------------- RUN CALCULATER WHEN BUTTON CLICKED ----------------------

controlButton = Button(root, text = "HESAPLA", width = 20, command = Calculate)
controlButton.config(font="bold")
controlButton.place(x=40,y=250)


root.mainloop()