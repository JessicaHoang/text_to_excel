'''
Program takes a text file than convert it to an excel file.
1. read text file
2. write as a csv file in the designated folder with delimiters
when reading the text file, read each line and have dictionary take in line 
number as the
How should I name the file?
Maybe prompt the user to the name.
'''

from dataclasses import dataclass
import pandas as pd
import re
import csv
import sys
from tkinter import *
'''
In Tkinter, everything is a widget.
Always a 2 step process: create it, than use it

'''

def GUI():
    root = Tk()
    # creating myLabel widget
    myLabel = Label(root, text="Hello world!")
    # showing it onto the screen
    myLabel.pack()
    # A constant loop shows the movement on the program
    root.mainloop()
    



def text_to_excel():
    # Path of where the file is located.
    textPath = r'C:\Users\khoa\Desktop\vscode_worksapce\text_to_excel\text\plushy_list.txt'
    # Path of where the csv file will end up
    csvPath = r'C:\Users\khoa\Desktop\vscode_worksapce\text_to_excel\excel\sample.csv'
    # Opening the file
    with open(textPath, 'r+') as file:
        dataframe1 = pd.read_csv(file, index_col=0, squeeze=True, sep='\t')
        dataframe1 = pd.DataFrame(dataframe1)
        Rows = []
        [Rows.append(row) for row in dataframe1.itertuples()]
        # dataframe1[['A', 'B']] = dataframe1[0].str.split(']', expand=True)
        # print(type(dataframe1))
        # Rows = list(filter(filterData, Rows))
        [print(row) for row in Rows]
        #print(Rows)
        # making more changes
        dataframe1.to_csv(csvPath)

   
if __name__ == "__main__":
    # text_to_excel()
    GUI()