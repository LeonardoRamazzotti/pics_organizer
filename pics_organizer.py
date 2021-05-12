#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 07:31:02 2021

@author: leonardo
"""
from tkinter import *
from tkinter import filedialog
import shutil # libreria che utiizzo per manipolare le stringhe e i folder
import os # libreria che mi permette di cancellare file o creare folder 

# Functions 

FolderName =''

TargetFolder =''

def choose_file_path():
    global FolderName
    FolderName = filedialog.askdirectory()
    file_loc.insert(0,FolderName)
    
def choose_target_path():
    global TargetFolder
    TargetFolder = filedialog.askdirectory()
    file_tg.insert(0,TargetFolder)
    
def Organize():
    file_path= file_loc.get()
    file_target= file_tg.get()
    file_detail= file_det.get()
    
    n_path = os.listdir(file_path)

    i = 0
    
    temp = file_target+'/temp/'
    
    
    os.makedirs(temp)

    while i < len(n_path):
        
        file_path_name = n_path[i]
        print(file_path_name)
        shutil.move(file_path+'/'+file_path_name,temp)
        i +=1 
        continue

    #creo una lista di tutti i file
    n_file = os.listdir(temp) #conto i file che ci sono nella mia directory

    print(n_file)

    # creo una lista con i dati da inserire per creare la directory
    data = file_detail.split(" ")

    #creo due cartelle per distinguere jpeg e raw
    os.makedirs(temp+data[2]+'/'+data[1]+'/'+data[0]+'/jpeg')
    os.makedirs(temp+data[2]+'/'+data[1]+'/'+data[0]+'/Raw')


    index =0

    file_list=[]
    
    jpeg_set={'.jpeg','.jpg','.JPG'}
    raw_set={'.CR2','.NEF','.PNG','.png'}

    #ciclo  che rinomina i file e , a seconda dell'estensione , gli mette nella giusta cartella
    while index < len(n_file) :
        #prendo dalla lista di file un file 
        file_name = n_file[index]
        #trasformo l'indice in una stringa per concatenarla al file e creare un seriale 
        est = os.path.splitext(file_name)
        ext = est[1]
        i=str(index)
       
        #condizione che a seconda dell' estensione mi stocca il file nella giusta directory
        if ext in jpeg_set :
            file = os.rename(temp+file_name,temp+file_detail+'-'+i+ext)
            file = file_detail+'-'+i+'.JPG'
            shutil.move(temp+file,temp+data[2]+'/'+data[1]+'/'+data[0]+'/jpeg')
        elif  ext in raw_set :
            file = os.rename(temp+file_name,temp+file_detail+'-'+i+ext)
            file = file_detail+'-'+i+ext
            shutil.move(temp+file,temp+data[2]+'/'+data[1]+'/'+data[0]+'/Raw')
    
        index+=1
        continue
    # sposto i file dalla cartella temp al main folder
    shutil.move(temp+data[2]+'/'+data[1]+'/'+data[0]+'/jpeg',file_target+'/'+data[2]+'/'+data[1]+'/'+data[0]+'/jpeg')
    shutil.move(temp+data[2]+'/'+data[1]+'/'+data[0]+'/Raw',file_target+'/'+data[2]+'/'+data[1]+'/'+data[0]+'/Raw')

    shutil.rmtree(temp+data[2])
    shutil.rmtree(temp)
    return

def Clear():
    file_loc.delete(0,'end')
    file_tg.delete(0,'end')
    file_det.delete(0,'end')
    return

# GUI Setup

root = Tk()

root.title('Pics Organizer')
root.geometry('300x500')
root.configure(background='#212121')
#root.iconbitmap(r'/media/leonardo/NIKON D200/Python/pics_organizer/icon.ico')

title = Label(text = 'Pics Organizer', width=40,bg ='#212121',fg='white')
title.grid(row=0,columnspan=2,padx=10,pady=10)

text_1 = Label(text='File Location Path:', width=20 ,bg ='#212121',fg='white' )
text_1.grid(row=1,column=0,pady=10)

file_loc= Entry(width=40,bg='#aaaaaa',fg='#212121')
file_loc.grid(row=2,columnspan=2,padx=5,pady=5)

loc_button = Button(root,text='Choose File Path', width=15,height=2,bg='#6d90ca', fg='#212121', command= choose_file_path)
loc_button.grid(row=3,columnspan=2,padx=10,pady=15)

text_2 = Label(text='File Location Target:', width=25 ,bg ='#212121',fg='white' )
text_2.grid(row=4,column=0,pady=10)

file_tg= Entry(width=40,bg='#aaaaaa',fg='#212121')
file_tg.grid(row=5,columnspan=2,padx=5,pady=5)

tg_button = Button(root,text='Choose Target Path', width=15,height=2,bg='#6d90ca', fg='#212121', command= choose_target_path)
tg_button.grid(row=6,columnspan=2,padx=10,pady=15)

text_3 = Label(text='File Details: (Event Month Year)', width=35 ,bg ='#212121',fg='white' )
text_3.grid(row=7,column=0,pady=10)

file_det= Entry(width=40,bg='#aaaaaa',fg='#212121')
file_det.grid(row=8,columnspan=2,padx=5,pady=5)

run = Button(root, text='Organize', width=10,height=2,bg='#6d90ca', fg='#212121', command=Organize)
run.grid(row=9,columnspan=2,padx=10,pady=15)

clear=Button(root,text='Clear', width=8,height=2,bg='#6d90ca', fg='#212121', command=Clear,)
clear.grid(row=10,columnspan=2,padx=10,pady=15)

root.mainloop()