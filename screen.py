from tkinter import *
from tkinter import filedialog
import cv2
from FaceDetection import *
from deepfake import *


class videoGUI:
    def __init__(self, window, window_title, size):
        self.window = window
        self.window.title(window_title)
        self.window.geometry(size)

        bottom_frame = Frame(self.window)
        bottom_frame.pack(side=TOP, pady=10)

        bot_frame = Frame(self.window)
        bot_frame.pack(side=TOP, pady=15)

        self.btn_select=Button(bottom_frame, text="Dosya Seçiniz", width=15, command=self.open_file, font=("Arial", 12))
        self.btn_select.grid(row=0, column=0)

        self.btn_sonuc=Button(bot_frame, text="Analiz", width=15, command=self.detec, font=("Arial", 12))
        self.btn_sonuc.grid(row=0, column=0)

        lbl_frame = Frame(self.window)
        lbl_frame.pack(side=TOP, pady=25)
        self.lbl=Label(lbl_frame, fg='#f00', pady=10, padx=10, font=("Arial", 15, "bold"))
        self.lbl.grid(row=0, column=0)

        self.delay = 5  
        self.window.mainloop()

    def open_file(self):
        self.filename = filedialog.askopenfilename(title="Select file", filetypes=(("MP4 files", "*.mp4"),
                    ("WMV files", "*.wmv"), ("AVI files", "*.avi"),("GİF files","*.gif")))
        self.cap = cv2.VideoCapture(self.filename)        
        return main(self.cap)
    
    def detec(self):
        self.lbl.config(text=detector())
        
    
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

videoGUI(Tk(), "DeepFake Detector","400x250")