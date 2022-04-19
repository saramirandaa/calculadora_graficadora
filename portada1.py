import tkinter

from tkinter import *
from PIL import Image, ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from math import *

def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)
# prSetTxt



class PlotWin:
    def botones(self, img, x, y, w, h):
        self.btn = tkinter.Button(self.window, text="START", command=self.btn01_click)
        self.btn.place(x=x, y=y, width=w, height = h)  
    #botones
    def fondos(self, ruta):
        self.portada = Image.open(ruta)
        self.test = ImageTk.PhotoImage(self.portada)

        self.label1 = tkinter.Label(image=self.test)
        self.label1.image = self.test
        
        self.label1.place(x=0, y=0)
    #fondos
    
    def createWindow(self):
        ancho = 960
        alto = 540
        coordenadas = str(ancho)+'x'+str(alto)
        self.window = tkinter.Tk()
        
        self.window.title("Proyecto Final POO")
        self.window.geometry(coordenadas)
        self.window.configure(bg='black')
        #self.window.attributes('-fullscreen', True) 
        
        self.portadadir = "/Users/saramiranda/Documents/PO/PROYECTO/portada.png"
        self.fondos(self.portadadir)
        
        #self.botones()

        self.window.mainloop()
    # createWindow
    
    def showPlot(self, pFunc, pRBeg, pREnd, pStep):
        lRBeg = -5
        if pRBeg != '':
            lRBeg = float(pRBeg)
        lREnd = 5
        if pREnd != '':
            lREnd = float(pREnd)
        lStep = 0.25
        if pStep != '':
            lStep = float(pStep)
            
        XVec = np.arange(lRBeg, lREnd, lStep)
        XSize = XVec.size
        YVec = np.arange(lRBeg, lREnd, lStep)
        YSize = YVec.size
        
        ZMat = np.zeros( (XSize, YSize) )
        
        for XIdx in range(0, XSize):
            for YIdx in range(0, YSize):
                X = XVec[XIdx]
                Y = YVec[YIdx]
                Z = eval(pFunc)
                #print(X, Y, Z)
                ZMat[XIdx, YIdx] = Z
        # ZMat
        
        XVecG, YVecG = np.meshgrid(XVec, YVec)
        
        lFig = Figure(figsize=(5, 4), dpi=120)
        lAxis = Axes3D(lFig)
        lAxis.plot_surface(XVecG, YVecG, ZMat,
                           rstride=1, cstride=1, 
                           cmap='plasma')
        
        lWin = tkinter.Tk()
        lWin.title(pFunc)
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, 
                                    fill=tkinter.BOTH, expand=1)
    # showPlot
    
    def btn01_click(self):
        self.func = (self.txt0A.get(), '*(X*X+Y*Y)')
        prSetTxt(self.txt01, self.func)
        self.showPlot(self.txt01.get(), self.txt02.get(),
                      self.txt03.get(), self.txt04.get())
    # btn01_click
    
# PlotWin

myPlotWin = PlotWin()
myPlotWin.createWindow()

