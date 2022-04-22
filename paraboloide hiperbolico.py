import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

from matplotlib.figure import Figure 

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


from math import *
import numpy as np 

def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)
#prSetTxt

class PlotWin:
    
    def createWindow(self):
        self.window = tkinter.Tk()
        
        self.window.title("Taller 3D")
        self.window.geometry("600x250+100+200")
        
        self.lbla =tkinter.Label(self.window, text="a= ")
        self.lbla.place(x=10, y=10)
        self.txta= tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txta.place(x=100, y=10)
        
        self.lblb =tkinter.Label(self.window, text="b= ")
        self.lblb.place(x=10, y=40)
        self.txtb= tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txtb.place(x=100, y=40)
        
        self.lbl02 = tkinter.Label(self.window, text= "límite inferior= ")
        self.lbl02.place(x=10, y=70)
        self.txt02 = tkinter.Entry(self.window, bg="lightgray", width = 50)
        self.txt02.place(x=100, y=70)
        prSetTxt(self.txt02, "-5") 
    
        self.lbl03 = tkinter.Label(self.window, text="límite superior=")
        self.lbl03.place(x=10, y=100)
        self.txt03 = tkinter.Entry(self.window, bg="lightgray", width = 50)
        self.txt03.place(x=100, y=100)
        prSetTxt(self.txt03, "5")
        
        self.lbl04= tkinter.Label(self.window, text="Recorrido= ")
        self.lbl04.place(x=10, y=130)
        self.txt04 = tkinter.Entry(self.window, bg="lightgray", width = 50)
        self.txt04.place(x=100, y=130)
        prSetTxt(self.txt04, "0.125")
        
     
        self.btn01 = tkinter.Button(self.window, text="Calcular", command=self.btn01_click)
        
        self.btn01.place(x=480, y=10, width=75)
        
        self.window.mainloop()
    
    def showPlot(self ,pA, pB, limS, limI, A):  
        
        XVec = np.arange(limS, limI, A)
        XSize = XVec.size
        
        YVec = np.arange(limS, limI, A)
        YSize = YVec.size
        
        ZMat = np.zeros( (XSize, YSize) ) 
        
        for XIdx in range(0, XSize): 
            for YIdx in range(0, YSize): 
                X = XVec[XIdx]
                Y = YVec[YIdx]
                Z= ((X**2/pA**2)-(Y**2/pB**2))
                
                ZMat[XIdx, YIdx] = Z
       
        XVecG, YVecG = np.meshgrid(XVec, YVec) 
        
        lFig = Figure(figsize=(5, 4), dpi=100) 
        lAxis = Axes3D(lFig) 
        lAxis.plot_surface(XVecG, YVecG, ZMat, rstride=1, cstride=1, cmap='inferno')
       
        
        
        lWin = tkinter.Tk()
        lWin.title(pA)
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
     
    
    def btn01_click(self):
        self.showPlot(float(self.txta.get()),  float(self.txtb.get()), float(self.txt02.get()), float(self.txt03.get()), float(self.txt04.get()))
        

myPlotWin = PlotWin()
myPlotWin.createWindow()