#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:45:09 2023

@author: viro
"""
'''
# this script is for the classification of t cell cytotoxic peptides
### Step1### The first step is to copy the peptides from excell sheet into csv file.
'''

############# convert peptides from csv file into a list using pandas  ###########

#import the library
import pandas as pd

#create a pandas dataframe
t_cell_pos = pd.read_csv("T_Cell_pos_17_Sept_2023.csv")

#print to see the content of the newly created dataframe
print(t_cell_pos)

#examine the type of the dataframe
type(t_cell_pos.shape)

#convert this dataframe (tupple) into list
t_cell_pos_lst = t_cell_pos["Epitope"].to_list()

#check the type of newly created list
type(t_cell_pos_lst)

#print this list
print(t_cell_pos_lst)

#print the length of this list
len(t_cell_pos_lst)
#1132

#it can be seen that the first element of the list is "name" which is not required.
t_cell_pos_lst.remove("Name")

#print the list with name removed
print(t_cell_pos_lst)

#check the length of the list with name removed
len(t_cell_pos_lst)
#1131

#####################################   processing negative dataset ###########################

#create a pandas dataframe
t_cell_neg = pd.read_csv("T_Cell_Neg_17_Sept_2023.csv")

#print to see the content of the newly created dataframe
print(t_cell_neg)

#examine the type of the dataframe
type(t_cell_neg.shape)

#convert this dataframe (tupple) into list
t_cell_neg_lst = t_cell_neg["Epitope"].to_list()

#check the type of newly created list
type(t_cell_neg_lst)

#print this list
print(t_cell_neg_lst)

#print the length of this list
len(t_cell_neg_lst)
#3123

#it can be seen that the first element of the list is "name" which is not required.
t_cell_neg_lst.remove("Name")

#print the list with name removed
print(t_cell_neg_lst)

#check the length of the list with name removed
len(t_cell_neg_lst)
#3122

#####################################   Removing dulplicates from pos and neg lists  ###########################

#removing the common peptides from both the lists

for i in t_cell_neg_lst[:]:
    if i in t_cell_pos_lst:
        t_cell_neg_lst.remove(i)
        t_cell_pos_lst.remove(i)
        
        
#checking the number of peptides left in positive and negative lists        

len(t_cell_pos_lst)        
#first it was 1132 and now it is 865

len(t_cell_neg_lst)
#first it was 3122 and now it is 2856

######### Remove the dulplictes from among the list using set function ####
tcell_pos_unique = list(set(t_cell_pos_lst))

len(tcell_pos_unique)
#864

#removal from negative list
tcell_neg_unique = (list(set(t_cell_neg_lst)))

len(tcell_neg_unique)
#2856

       
#####################################   Removing peptides containing unnatural amino acids ###########################
import protlearn

from protlearn.preprocessing import remove_unnatural

### since protlearn runds in python console in terminal hence we need to write these peptides into files. These
#files will then be fed into protlearn.

# writting the peptide sequences into a text file for positive dataset
with open ("tcell_pos_unique.txt", "w") as wf:
    for i in tcell_pos_unique:
        wf.write(i + "\n")
        

# writting the peptide sequences into a text file for negative dataset
with open ("tcell_neg_unique.txt", "w") as wf:
    for i in tcell_neg_unique:
        wf.write(i + "\n")





il17_pos_unique = remove_unnatural(il17_pos_unique)

len(il17_pos_unique)
#658









df_pos = pd.read_csv("T_cell_cytox_pos.csv")
df_neg = pd.read_csv("T_cell_cytox_neg.csv")

df_pos.shape
df_neg.shape
tcyt_pos = df_pos["Epitope"].tolist()
tcyt_neg = df_neg["Epitope"].tolist()


for i in tcyt_neg[:]:
    if i in tcyt_pos:
        tcyt_neg.remove(i)

tcyt_pos_uniq = list(set(tcyt_pos))
tcyt_neg_uniq = list(set(tcyt_neg))        

with open ("tcyt_pos1", "w") as wf:
    for i in tcyt_pos_uniq:
        wf.write(i + "\n)
    