# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:19:49 2020

@author: Nadile
"""

notes=[90,34,56,76]
type(notes) ##list
liste=["hello world",34,56,10.39]
liste2=[liste,notes] #ikisini kapsar
len(liste2) #iki liste 1 eleman olarak sayar yani 2
del liste2 # liste2 yi siler

liste[2] #56
liste[3] #10.39

liste[0:3] #['hello world', 34, 56]
liste[:3] #['hello world', 34, 56]
liste[2:] #[56, 10.39]

new_list=["a",10,[20,30,40,50]]
new_list[2][1] #30
names=["ali","veli","ayse","ayla"]
names[1]="velinin annesi"
print(names)
names[1]="veli"
names[0:3]="alinin_babası","velinin_babası","aysenin_babası","aylanın_babası"
names #yeni liste ['alinin_babası', 'velinin_babası', 'aysenin_babası', 'aylanın_babası', 'ayla']


names=["ali","veli","ayse","ayla"]
names=names+["kemal"]
names

dir(names) # names yani liste ile ilgili metotları gösterir

names.append("beril") #isim ekleme
names.remove("ayse") #isim çıkarma

names=["ali","veli","ayse","ayla"]
names.insert(0,"deneme")

names.insert(len(names),"beren") #listenin sonuna elemanı ekler.
names
names.pop(0) # o. indeksteki elemanı silme


names.count("ali") #1 tane

names_copy=names.copy() #names, names_copy adında listeye kopyalandı.

names.extend(["a","v",4]) #♦names listesiyle birleşti.

names.index("veli") #veli 1.indekste

names.reverse() #listeyi tersine çevirdi

liste2=[10,40,5,15,3]
liste2.sort() #listeyi sıralar küçükten büyüğe

liste2.clear() #liste içeriğini siler






















