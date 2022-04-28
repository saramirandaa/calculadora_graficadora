import tkinter
import os
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
        pass
    #botones
    
    def fondos(self, ruta):
        self.portada = Image.open(ruta)
        self.test = ImageTk.PhotoImage(self.portada)

        self.label1 = tkinter.Label(image=self.test)
        self.label1.image = self.test
        
        self.label1.place(x=-1, y=0)
    #fondos
    
    def createWindow(self):
        ancho = 960
        alto = 540
        coordenadas = str(ancho)+'x'+str(alto) + '+100+200'
        self.window = tkinter.Tk()
        
        self.window.title("Proyecto Final POO")
        self.window.geometry(coordenadas)
        #self.window.configure(bg='black')
        #self.window.attributes('-fullscreen', True) 
        
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/portada.png"
        self.fondos(self.portadadir)
        
        self.btn01 = tkinter.Button(self.window, borderwidth = 5, text="INICIO", 
                                    command=self.menu)
        self.btn01.place(x=450, y=320, height = 50, width=100)
        
        #self.botones()

        self.window.mainloop()
    # createWindow

    def menu(self):
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/menu.png"
        self.fondos(self.portadadir)
        self.botones_menu()
    # btn01_click
    def botones_menu(self):
        self.elip = tkinter.Button(self.window, borderwidth = 0, 
                                    command=self.elipsoide)
        self.elip.place(x=93, y=140, height = 20, width=20)
        
        self.par_elip = tkinter.Button(self.window, borderwidth = 0, 
                                    command=self.paraboloide_eliptico)
        self.par_elip.place(x=93, y=227, height = 20, width=20)
        #--------------------------
        self.par_hip = tkinter.Button(self.window, borderwidth = 0, 
                                    command=self.paraboloide_hiper)
        self.par_hip.place(x=93, y=315, height = 20, width=20)
        #______________________________
        self.cil_hip = tkinter.Button(self.window, borderwidth = 0, 
                                    command=self.cilindro_hiperbolico)
        self.cil_hip.place(x=93, y=405, height = 20, width=20)
        
        self.cono = tkinter.Button(self.window, borderwidth = 0, 
                                    command=self.conoelip)
        self.cono.place(x=530, y=140, height = 20, width=20)
        #_____________
        self.hip2 = tkinter.Button(self.window, borderwidth = 0, 
                                    command=self.hiperboloide_doshojas)
        self.hip2.place(x=530, y=227, height = 20, width=20)
        #______________________________
        self.historial = tkinter.Button(self.window, borderwidth = 0, 
                                    command=self.historial)
        self.historial.place(x=530, y=315, height = 20, width=20)
    #botones_menu
    
    def salir(self):
        self.back = tkinter.Button(self.window, borderwidth = 0, text = "MENU",
                                    command=self.menu)
        self.back.place(x=850, y=450, height = 50, width=75)
    #salir
    def parametros(self):
        self.lblX = tkinter.Label(self.window, text="X = ", bg="black", fg ="white")
        self.lblX.place(x=200, y=352)
        self.txtX = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtX.place(x=250, y=350)
        prSetTxt(self.txtX, '1')
        
        self.lblY = tkinter.Label(self.window, text="Y = ", bg="black", fg ="white")
        self.lblY.place(x=200, y=392)
        self.txtY = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtY.place(x=250, y=390)
        prSetTxt(self.txtY, '2')
        
        self.lblA = tkinter.Label(self.window, text="a = ", bg="black", fg ="white")
        self.lblA.place(x=200, y=432)
        self.txtA = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtA.place(x=250, y=430)
        prSetTxt(self.txtA, '5')
        
        self.lblB = tkinter.Label(self.window, text="b = ", bg="black", fg ="white")
        self.lblB.place(x=200, y=472)
        self.txtB = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtB.place(x=250, y=470)
        prSetTxt(self.txtB, '4')
        
        self.lblstep = tkinter.Label(self.window, text="step = ", bg="black", fg ="white")
        self.lblstep.place(x=50, y=352)
        self.txtstep = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtstep.place(x=100, y=350)
        prSetTxt(self.txtstep, '0.50')
        
        self.lblRi = tkinter.Label(self.window, text="Ri = ", bg="black", fg ="white")
        self.lblRi.place(x=50, y=392)
        self.txtRi = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtRi.place(x=100, y=390)
        prSetTxt(self.txtRi, '-10')
        
        self.lblRf = tkinter.Label(self.window, text="Rf = ", bg="black", fg ="white")
        self.lblRf.place(x=50, y=432)
        self.txtRf = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtRf.place(x=100, y=430)
        prSetTxt(self.txtRf, '10')
    #parametros

    
    def paraboloide_hiper(self):
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/parhip.png"
        self.fondos(self.portadadir)
        #------parametros-------
        self.parametros()
        
        #funcion = str(self.txtX.get()) + '+' + str(self.txty.get())
        self.lblZ = tkinter.Label(self.window, text="Z = ", bg="black", fg ="white")
        self.lblZ.place(x=350, y=352)
        
        a = (float(self.txtA.get()) * float(self.txtA.get()))
        b = (float(self.txtB.get()) * float(self.txtB.get()))
        funcion = ('(',self.txtY.get(), '*Y*Y/', str(b), ')-(', 
                   self.txtX.get(), '*X*X/', str(a),')' )
        self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=352)
        
        
        self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                    command=self.btngraph1)
        self.graph.place(x=650, y=352, height = 50, width=75)
        
        self.salir()
    #paraboloide_hiper
    def btngraph1(self):
        a = (float(self.txtA.get()) * float(self.txtA.get()))
        b = (float(self.txtB.get()) * float(self.txtB.get()))
        funcion = ('(',self.txtY.get(), '*Y*Y/', str(b), ')-(', 
                   self.txtX.get(), '*X*X/', str(a),')' )
        self.txtfunc = tkinter.Entry(self.window, borderwidth = 0, bg="black", fg ="black", width=5)
        self.txtfunc.place(x=980, y=430)
        prSetTxt(self.txtfunc, funcion)
        
        self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=352)
        
        self.showPlot(self.txtfunc.get(), self.txtRi.get(),
                      self.txtRf.get(), self.txtstep.get(),0, 'Paraboloide Hiperbólico')
    #btngraph1
    
    
    def hiperboloide_doshojas(self):
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/hiper2.png"
        self.fondos(self.portadadir)
        
        self.parametros()
        
        self.lblZ = tkinter.Label(self.window, text="Z = ", bg="black", fg ="white")
        self.lblZ.place(x=350, y=352)
        self.txtZ = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtZ.place(x=400, y=350)
        prSetTxt(self.txtZ, '4')
        
        self.lblC = tkinter.Label(self.window, text="C = ", bg="black", fg ="white")
        self.lblC.place(x=350, y=392)
        self.txtC = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtC.place(x=400, y=390)
        prSetTxt(self.txtC, '2')
        
        self.lblF = tkinter.Label(self.window, text="-1 = ", bg="black", fg ="white")
        self.lblF.place(x=350, y=432)
        
        a = (float(self.txtA.get()) * float(self.txtA.get()))
        b = (float(self.txtB.get()) * float(self.txtB.get()))
        c = (float(self.txtC.get()) * float(self.txtC.get()))
        funcion = ('(',self.txtX.get(), '*X*X/', str(a), ')+(', 
                   self.txtY.get(), '*Y*Y/', str(b),')', '-(', self.txtZ.get(), '*Z*Z/',str(c),')' )
        self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        
        self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                    command=self.btngraph2)
        self.graph.place(x=650, y=352, height = 50, width=75)
        
        self.salir()
    #hiperboloide_doshojas
    
    def btngraph2(self):
        a = (float(self.txtA.get()) * float(self.txtA.get()))
        b = (float(self.txtB.get()) * float(self.txtB.get()))
        c = (float(self.txtC.get()) * float(self.txtC.get()))
        funcion = ('(',self.txtX.get(), '*X*X/', str(a), ')+(', 
        self.txtY.get(), '*Y*Y/', str(b),')', '-(', self.txtZ.get(), '*Z*Z/',str(c),')' )
       
        funcion2 = ('(',str(c),'*((',self.txtX.get(), '*X*X/', str(a), ')+(', 
        self.txtY.get(), '*Y*Y/', str(b),')', '+1))**0.5' )
        
        self.txtfunc = tkinter.Entry(self.window, borderwidth = 0, bg="black", fg ="black", width=5)
        self.txtfunc.place(x=980, y=430)
        prSetTxt(self.txtfunc, funcion2)
        
        self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        self.showPlot(self.txtfunc.get(), self.txtRi.get(),
                      self.txtRf.get(), self.txtstep.get(),1, 'Hiperboloide de dos hojas')
    #btngraph1
    
    def elipsoide(self):
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/elipsoide.png"
        self.fondos(self.portadadir)
        self.parametros()
        
        self.salir()
    #elipsoide
    
    
    def paraboloide_eliptico(self):
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/parel.png"
        self.fondos(self.portadadir)
        self.parametros()
        
        self.salir()
    #paraboloide_eliptico
    
    def cilindro_hiperbolico(self):
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/cilhip.png"
        self.fondos(self.portadadir)
        self.parametros()
        
        self.lblZ = tkinter.Label(self.window, text="Z = ", bg="black", fg ="white")
        self.lblZ.place(x=350, y=352)
        self.txtZ = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtZ.place(x=400, y=350)
        prSetTxt(self.txtZ, '4')
        
        self.lblF = tkinter.Label(self.window, text="1 = ", bg="black", fg ="white")
        self.lblF.place(x=350, y=432)
        
        a = (float(self.txtA.get()) * float(self.txtA.get()))
        b = (float(self.txtB.get()) * float(self.txtB.get()))
        
        funcion = ('(',self.txtX.get(), '*X*X/', str(a), ')-(', 
                   self.txtY.get(), '*Y*Y/', str(b),')')
        self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        
        self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                    command=self.btngraph5)
        self.graph.place(x=650, y=352, height = 50, width=75)
        
        self.salir()
    #cilindro_hiperbolico
    def btngraph5(self):
        a = (float(self.txtA.get()) * float(self.txtA.get()))
        b = (float(self.txtB.get()) * float(self.txtB.get()))
        
        funcion = ('(',self.txtX.get(), '*X*X/', str(a), ')-(', 
        self.txtY.get(), '*Y*Y/', str(b),')')
       
        funcion2 = ('((',self.txtX.get(), '*X*X/',str(a),')-(',
        self.txtY.get(), '*Y*Y/', str(b),'))-1')
        
        self.txtfunc = tkinter.Entry(self.window, borderwidth = 0, bg="black", fg ="black", width=5)
        self.txtfunc.place(x=980, y=430)
        prSetTxt(self.txtfunc, funcion2)
        
        self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        self.showPlot(self.txtfunc.get(), self.txtRi.get(),
                      self.txtRf.get(), self.txtstep.get(),1, 'Cilindro hiperbólico')
    def conoelip(self):
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/conoelip.png"
        self.fondos(self.portadadir)
        self.parametros()
        
        self.lblZ = tkinter.Label(self.window, text="Z = ", bg="black", fg ="white")
        self.lblZ.place(x=350, y=352)
        self.txtZ = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtZ.place(x=400, y=350)
        prSetTxt(self.txtZ, '4')
        
        self.lblC = tkinter.Label(self.window, text="C = ", bg="black", fg ="white")
        self.lblC.place(x=350, y=392)
        self.txtC = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtC.place(x=400, y=390)
        prSetTxt(self.txtC, '2')
        
        self.lblF = tkinter.Label(self.window, text="Z = ", bg="black", fg ="white")
        self.lblF.place(x=350, y=432)
        
        a = (float(self.txtA.get()) * float(self.txtA.get()))
        b = (float(self.txtB.get()) * float(self.txtB.get()))
        c = (float(self.txtC.get()) * float(self.txtC.get()))
        funcion = ("sqrt(",('(',self.txtX.get(), '*X*X/', str(a), ')+(', 
                   self.txtY.get(), '*Y*Y/', str(b),')'),"*",str(c),")")
        self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        
        self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                    command=self.btngraph6)
        self.graph.place(x=650, y=352, height = 50, width=75)
        self.salir()
    #cono
    def btngraph6(self):
        a = (float(self.txtA.get()) * float(self.txtA.get()))
        b = (float(self.txtB.get()) * float(self.txtB.get()))
        c = (float(self.txtC.get()) * float(self.txtC.get()))
        funcion =('(',str(c),'*((',self.txtX.get(), '*X*X/', str(a), ')+(', 
        self.txtY.get(), '*Y*Y/', str(b),'))**0.5' )
        
       
        funcion2 = ('(',str(c),'*(',self.txtX.get(), '*X*X/', str(a), ')+(', 
        self.txtY.get(), '*Y*Y/', str(b),'))**0.5' )
        
        self.txtfunc = tkinter.Entry(self.window, borderwidth = 0, bg="black", fg ="black", width=5)
        self.txtfunc.place(x=980, y=430)
        prSetTxt(self.txtfunc, funcion2)
        
        self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        self.showPlot(self.txtfunc.get(), self.txtRi.get(),
                      self.txtRf.get(), self.txtstep.get(),1, 'Cono elíptico')
    def historial(self):
        self.portadadir = "/Users/LUZ DEL CARMEN/Documents/Fer universidad/POO proyecto/portada.png"
        self.fondos(self.portadadir)
        
        
        self.salir()
    #historial
    def showPlot(self, pFunc, pRBeg, pREnd, pStep, band, grafica):
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
        funcion = pFunc

        for XIdx in range(0, XSize):
            for YIdx in range(0, YSize):
                X = XVec[XIdx]
                Y = YVec[YIdx]
                Z = eval(funcion)
                #print(X, Y, Z)
                ZMat[XIdx, YIdx] = Z
                
        # ZMat
        
        XVecG, YVecG = np.meshgrid(XVec, YVec)
        
        lFig = Figure(figsize=(5, 4), dpi=120)
        lAxis = Axes3D(lFig)
        lAxis.plot_surface(XVecG, YVecG, ZMat,
                           rstride=1, cstride=1, 
                           cmap='plasma')
        if(band == 1):
            for XIdx in range(0, XSize):
                for YIdx in range(0, YSize):
                    X = XVec[XIdx]
                    Y = YVec[YIdx]
                    Z = eval(funcion)
                    ZMat[XIdx, YIdx] = -Z
                    

            lAxis.plot_surface(XVecG, YVecG, ZMat,
                               rstride=1, cstride=1, 
                               cmap='plasma') 
        
        lWin = tkinter.Tk()
        lWin.title(grafica)
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, 
                                    fill=tkinter.BOTH, expand=1)
    # showPlot
# PlotWin

myPlotWin = PlotWin()
myPlotWin.createWindow()