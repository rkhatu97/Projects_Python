# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:57:37 2020

@author: rkhat
"""

from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageChops
import pytesseract
import cv2

class ReadFileApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Open Image")
        self.label.grid(row = 0, column = 2, columnspan = 2)
        
        ttk.Button(master, text = "Open File",
                   command = self.select_file).grid(row = 2, column = 2)

        self.label = ttk.Label(master, text = "Display Image Content")
        self.label.grid(row = 3, column = 2, columnspan = 2)

        ttk.Button(master, text = "Print the Content",
                   command = self.count_occurrences).grid(row = 4, column = 2)    

        self.label = ttk.Label(master, text = "Save In File")
        self.label.grid(row = 5, column = 2, columnspan = 2)
        
        ttk.Button(master, text = "Write the Content",
                   command = self.write_files).grid(row = 6, column = 2) 

        self.label = ttk.Label(master, text = "Quit Window")
        self.label.grid(row = 7, column = 2, columnspan = 2)        
        
        ttk.Button(master, text = "Quit",
                   command = master.destroy).grid(row = 8, column = 2) 
        
    def select_file(self):
            self.filename = filedialog.askopenfilename(initialdir=".")
            self.infile = open(self.filename, "r")
            self.label_1 = ttk.Label(None, text = self.infile.name)
            self.label_1.grid(row = 10, column = 2)


    def count_occurrences(self):
                im_gray = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
                (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                thresh = 127
                im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
                self.tex = pytesseract.image_to_string(im_bw, lang = 'eng')
                self.label_2 = ttk.Label(None, text = self.tex)
                self.label_2.grid(row = 12, column = 2)
                
    def write_files(self):
             files = [('All Files', '*.*'),  
                      ('Python Files', '*.py'), 
                      ('Text Document', '*.txt')]
             file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
             file.write(self.tex + '\n')
             file.close()
             

def main():              
    main = Tk()
    main.geometry('400x500')
    main.title("OCR Application")
    main.iconbitmap(default='C:\\Users\\rkhat\\Downloads\\o.ico')
    app = ReadFileApp(main)
    main.mainloop()
    
if __name__ == "__main__": main()