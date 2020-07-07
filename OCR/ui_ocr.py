# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:57:37 2020

@author: rkhat
"""

from tkinter import *
from tkinter import ttk, filedialog, messagebox
import pytesseract
import cv2

class ReadFileApp:
    master=None
    
    def __init__(self, master):
        self.master=master
        self.x_start, self.y_start, self.x_end, self.y_end = 0, 0, 0, 0
        self.cropping = False
        
        self.label = ttk.Label(master, text = "Open Image")
        self.label.grid(row = 0, column = 1)
        
        ttk.Button(master, text = "Open File",
                   command = self.select_file).grid(row = 2, column = 1)

        self.label = ttk.Label(master, text = "Display Image Content")
        self.label.grid(row = 0, column = 2)

        ttk.Button(master, text = "Print the Content",
                   command = self.img_conver).grid(row = 2, column = 2)
        

        self.label = ttk.Label(master, text = "Save In File")
        self.label.grid(row = 0, column = 3)
        
        ttk.Button(master, text = "Write the Content",
                   command = self.write_files).grid(row = 2, column = 3) 

        self.label = ttk.Label(master, text = "Clear Labels")
        self.label.grid(row = 3, column = 1)        
        
        ttk.Button(master, text = "Clear Labels",
                   command = self.clear_widget).grid(row = 4, column = 1)
        
        self.label = ttk.Label(master, text = "Quit Window")
        self.label.grid(row = 3, column = 2)        
        
        ttk.Button(master, text = "Quit",
                   command = master.destroy).grid(row = 4, column = 2)
        
        
    def select_file(self):
            self.filename = filedialog.askopenfilename(initialdir=".")
            self.infile = open(self.filename, "r")
            self.label_3 = ttk.Label(None, text = self.infile.name)
            self.label_3.grid(row = 5, column = 2)
            
    def mouse_crop(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.x_start, self.y_start, self.x_end, self.y_end = x, y, x, y
            self.cropping = True
 

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.cropping == True:
                self.x_end, self.y_end = x, y
 
  
        elif event == cv2.EVENT_LBUTTONUP:

            self.x_end, self.y_end = x, y
            self.cropping = False 
 
            refPoint = [(self.x_start, self.y_start), (self.x_end, self.y_end)]
            
            if len(refPoint) == 2: 
                self.roi = self.oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
                cv2.imshow("Cropped", self.roi)
                self.im_bw = self.roi

    def img_conver(self):
        try:
                self.im_gray = cv2.imread(self.filename, cv2.IMREAD_GRAYSCALE)
                (thresh, self.im_bw) = cv2.threshold(self.im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                thresh = 127
                self.im_bw = cv2.threshold(self.im_bw, thresh, 255, cv2.THRESH_BINARY)[1]
                cv2.imshow('Press Q To Close', self.im_bw)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                self.oriImage = self.im_bw
                self.mSgBox = messagebox.askquestion('Image Crop','Do you want to crop the image',icon = 'warning')
                if self.mSgBox == 'yes':
                    cv2.namedWindow("image")
                    cv2.setMouseCallback("image", self.mouse_crop) 
                    while True:
                        i = self.im_bw.copy()
                        if not self.cropping:
                            cv2.imshow("image", i)
                        elif self.cropping:
                            cv2.rectangle(i, (self.x_start, self.y_start), (self.x_end, self.y_end), (255, 0, 0), 2)
                            cv2.imshow("image", i)
                        k = cv2.waitKey(1) & 0xFF 
                        if k == ord('q'):
                            break
                    cv2.destroyAllWindows()
                    self.label_1 = ttk.Label(None, text = "Image Cropped")
                    self.label_1.grid(row = 6, column = 2)
                else:
                    messagebox.showinfo('Return','You will now return to the application screen')
                self.MsgBox = messagebox.askquestion('Image Invert','Do you want to invert the image',icon = 'warning')
                if self.MsgBox == 'yes':
                    self.im_bw = cv2.bitwise_not(self.im_bw)
                    cv2.imshow('Press Q To Close', self.im_bw)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    self.tex = pytesseract.image_to_string(self.im_bw, lang = 'eng')
                    try:
                        self.label_1.configure(None, text = "Text Extracted")
                    except AttributeError:
                        self.label_1 = ttk.Label(None, text = "Text Extracted")
                    self.label_1.grid(row = 6, column = 2)
                else:
                    messagebox.showinfo('Return','You will now return to the application screen')
                self.tex = pytesseract.image_to_string(self.im_bw, lang = 'eng')   
                try:
                    self.label_1.configure(None, text = "Text Extracted")
                except AttributeError:
                    self.label_1 = ttk.Label(None, text = "Text Extracted")
                self.label_1.grid(row = 6, column = 2)
        except AttributeError:
             self.label_1 = ttk.Label(None, text = "Please Provide An Image", foreground = "red")
             self.label_1.grid(row = 7, column = 2)
        except:
             self.label_1 = ttk.Label(None, text = "Something went wrong..!!", foreground = "red")
             self.label_1.grid(row = 7, column = 2)

                
        
    def clear_widget(self):
        try:
            try:
                self.label_1.destroy()
                self.label_3.destroy()
            except AttributeError:     
                self.label_3.destroy()
        except AttributeError:
            self.label_1 = ttk.Label(None, text = "Label Not Yet Created", foreground = "red")
            self.label_1.grid(row = 7, column = 2)
        except:
            self.label_1 = ttk.Label(None, text = "Something went wrong..!!", foreground = "red")
            self.label_1.grid(row = 7, column = 2)
        
                
    def write_files(self):
        try:
             files = [('All Files', '*.*'),  
                      ('Python Files', '*.py'), 
                      ('Text Document', '*.txt')]
             file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
             file.write(self.tex + '\n')
             file.close()
             if file:
                 try:
                     self.label_1.configure(None, text = "File Saved")
                 except AttributeError:
                    self.label_1 = ttk.Label(None, text = "File Saved")
                 self.label_1.grid(row = 6, column = 2)
             self.msgBox = messagebox.askquestion('Quit','Do you want to quit',icon = 'warning')
             if self.msgBox == 'yes':
                   self.master.destroy()
             else:
                    messagebox.showinfo('Return','You will now return to the application screen')
                    self.clear_widget()
        except AttributeError:            
             self.label_1 = ttk.Label(None, text = "Nothing To Save", foreground = "red")
             self.label_1.grid(row = 7, column = 2)

        except:
             self.label_1 = ttk.Label(None, text = "Something went wrong..!!", foreground = "red")
             self.label_1.grid(row = 7, column = 2)


                    

def main():              
    main = Tk()
    main.geometry('500x500')
    main.title("OCR Application")
    main.iconbitmap(default='C:\\Users\\rkhat\\Downloads\\icon.ico')
    app = ReadFileApp(main)
    main.mainloop()
    
if __name__ == "__main__": main()