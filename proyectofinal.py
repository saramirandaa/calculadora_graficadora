import tkinter
import os
#from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#import math
# mport json

#******************************************************************************
portada = "/Users/saramiranda/Documents/PO/PROYECTO/portada.png"
menu = "/Users/saramiranda/Documents/PO/PROYECTO/menu.png"
parhip = "/Users/saramiranda/Documents/PO/PROYECTO/parhip.png"
hiper2 = "/Users/saramiranda/Documents/PO/PROYECTO/hiper2.png"
elipsoide = "/Users/saramiranda/Documents/PO/PROYECTO/elipsoide.png"
parel = "/Users/saramiranda/Documents/PO/PROYECTO/parel.png"
cilhip = "/Users/saramiranda/Documents/PO/PROYECTO/cilhip.png"
conoelip = "/Users/saramiranda/Documents/PO/PROYECTO/conoelip.png"
historial = "/Users/saramiranda/Documents/PO/PROYECTO/historial.png"


def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)
# prSetTxt

class Graficador(): 
    def showPlot(self, pFunc, pRBeg, pREnd, pStep, band, grafica, colmap):
        
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
                           cmap= colmap)
        
        if(band == 1):
            for XIdx in range(0, XSize):
                for YIdx in range(0, YSize):
                    X = XVec[XIdx]
                    Y = YVec[YIdx]
                    Z = eval(funcion)
                    ZMat[XIdx, YIdx] = -Z
            lAxis.plot_surface(XVecG, YVecG, ZMat,
                               rstride=1, cstride=1, 
                               cmap=colmap) 
        
        lWin = tkinter.Tk()
        lWin.title(grafica)
        lWin.configure(bg='black')
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas._tkcanvas.config(bg="black")
        canvas.get_tk_widget().pack(side=tkinter.TOP, 
                                    fill=tkinter.BOTH, expand=1)
        
    # showPlot
#class Graficador
class PlotWin(Graficador): #botones, graficas e imagenes

    
    def fondos(self, ruta):
        self.portada = Image.open(ruta)
        self.test = ImageTk.PhotoImage(self.portada)
    
        self.label1 = tkinter.Label(image=self.test)
        self.label1.image = self.test
        
        self.label1.place(x=-1, y=0)
    #fondos
    def selection_changed(self,event):
        selection = self.combo.get()
        if (selection == 'Pastel'):
            self.colmap = 'Pastel1'
        elif(selection == 'Rojo'):
            self.colmap = 'autumn'
        elif(selection == 'Rosa'):
            self.colmap = 'spring'
        elif(selection == 'Negro'):
            self.colmap = 'binary'
        elif(selection == 'Arcoiris'):
            self.colmap = 'gist_ncar'
        elif(selection == 'Azul'):
            self.colmap = 'ocean'
        elif(selection == 'Verde'):
            self.colmap = 'viridis'
        
    def colores(self):
        self.combo = ttk.Combobox(
            state="readonly",
            values=["Azul", "Rojo", "Rosa", "Negro", "Verde", "Arcoiris", "Pastel"])
        self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
        self.combo.set('Azul')
        self.combo.place(x=550, y=480)
    def createWindow(self):
        ancho = 960
        alto = 540
        coordenadas = str(ancho)+'x'+str(alto) + '+100+200'
        self.window = tkinter.Tk()
        
        self.window.title("Proyecto Final POO")
        self.window.geometry(coordenadas)
        
        self.portadadir = portada
        self.fondos(self.portadadir)
        
        self.btn01 = tkinter.Button(self.window, borderwidth = 5, text="INICIO", 
                                    command=self.menu)
        self.btn01.place(x=450, y=320, height = 50, width=100)
        
        self.window.mainloop()
    # createWindow
    def menu(self):
        self.portadadir = menu
        self.fondos(self.portadadir)
        self.botones_menu()
    def salir(self):
        self.back = tkinter.Button(self.window, borderwidth = 0, text = "MENU",
                                    command=self.menu)
        self.back.place(x=850, y=450, height = 50, width=75)
    #salir
    def botones_menu(self):
        self.hist = tkinter.Button(self.window, borderwidth = 0, 
                                    command=self.historial)
        self.hist.place(x=530, y=315, height = 20, width=20)
        
        #----------------------------
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
        
    #botones_menu
    def parametros(self, band, band2):
        self.colores()
        
        self.lblX = tkinter.Label(self.window, text="X = ", bg="black", fg ="white")
        self.lblX.place(x=200, y=352)
        self.txtX = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtX.place(x=250, y=350)
        prSetTxt(self.txtX, '1')
        
        self.lblY = tkinter.Label(self.window, text="Y = ", bg="black", fg ="white")
        self.lblY.place(x=200, y=392)
        self.txtY = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtY.place(x=250, y=390)
        prSetTxt(self.txtY, '1')
        
        self.lblA = tkinter.Label(self.window, text="a = ", bg="black", fg ="white")
        self.lblA.place(x=200, y=432)
        self.txtA = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtA.place(x=250, y=430)
        prSetTxt(self.txtA, '1')
        
        self.lblB = tkinter.Label(self.window, text="b = ", bg="black", fg ="white")
        self.lblB.place(x=200, y=472)
        self.txtB = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtB.place(x=250, y=470)
        prSetTxt(self.txtB, '1')
        
        self.lblstep = tkinter.Label(self.window, text="step = ", bg="black", fg ="white")
        self.lblstep.place(x=50, y=352)
        self.txtstep = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
        self.txtstep.place(x=100, y=350)
        prSetTxt(self.txtstep, '0.25')
        
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
        
        self.lblZ = tkinter.Label(self.window, text="Z = ", bg="black", fg ="white")
        self.lblZ.place(x=350, y=430)
        
        if (band == 1): # 1 = XYZ CON ABC
            self.lblZ = tkinter.Label(self.window, text="Z = ", bg="black", fg ="white")
            self.lblZ.place(x=350, y=352)
            self.txtZ = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
            self.txtZ.place(x=400, y=350)
            prSetTxt(self.txtZ, '1')
            
            self.lblC = tkinter.Label(self.window, text="C = ", bg="black", fg ="white")
            self.lblC.place(x=350, y=392)
            self.txtC = tkinter.Entry(self.window, bg="black", fg ="white", width=5)
            self.txtC.place(x=400, y=390)
            prSetTxt(self.txtC, '1')
            
        if (band2 == 1): # Z = X + Y CON ABC
            self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                        command=self.btngraph1)
            self.graph.place(x=650, y=352, height = 50, width=75)
        elif(band2 == 2): # 1 = XYZ CON ABC
            self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                        command=self.btngraph2)
            self.graph.place(x=650, y=352, height = 50, width=75)
            
    #parametros
    def gets(self, ec):
        self.a = (float(self.txtA.get()) * float(self.txtA.get()))
        self.b = (float(self.txtB.get()) * float(self.txtB.get()))
        if((self.a  == 0) or (self.b == 0)):
            messagebox.showinfo(
                title="ERROR",
                message="El numero no debe ser CERO")
        
        if(ec==1):
            self.funcion = ('(',self.txtY.get(), '*Y*Y/', str(self.b), ')-(', 
                       self.txtX.get(), '*X*X/', str(self.a),')' )
        elif(ec==2):
            self.c = (float(self.txtC.get()) * float(self.txtC.get()))
            self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
                      self.txtY.get(), '*Y*Y/', str(self.b),')', '-(', self.txtZ.get(), '*Z*Z/',str(self.c),')' )
        elif(ec==3):
            self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
                       self.txtY.get(), '*Y*Y/', str(self.b),')')
        elif(ec==4):
            self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
                       self.txtY.get(), '*Y*Y/', str(self.b),')')
        elif(ec==5):
            self.c = (float(self.txtC.get()) * float(self.txtC.get()))
            self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
                       self.txtY.get(), '*Y*Y/', str(self.b),')*Z*Z/',str(self.c),')')
            
        self.lblf = tkinter.Label(self.window, text=self.funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
    def btngraph1(self): #grafica directamente la funcion
        
        ecuacion = self.ec
        self.gets(ecuacion)
        self.txtfunc = tkinter.Entry(self.window, borderwidth = 0, bg="black", fg ="black", width=5)
        self.txtfunc.place(x=980, y=430)
        prSetTxt(self.txtfunc, self.funcion)
        
        self.showPlot(self.txtfunc.get(), self.txtRi.get(),
            self.txtRf.get(), self.txtstep.get(),0, self.nombre, self.colmap)
        
    #btngraph1
    
    def btngraph2(self): #lleva una funcion2 que es la que grafica
        ecuacion = self.ec
        self.gets(ecuacion)
        self.txtfunc = tkinter.Entry(self.window, borderwidth = 0, bg="black", fg ="black", width=5)
        self.txtfunc.place(x=980, y=430)
        prSetTxt(self.txtfunc, self.funcion2)
        
        self.showPlot(self.txtfunc.get(), self.txtRi.get(),
                      self.txtRf.get(), self.txtstep.get(),1, self.nombre, self.colmap)
    #btngraph2
            
    def paraboloide_hiper(self): #LISTOOO 2,0  1
        self.portadadir = parhip
        self.fondos(self.portadadir)
        #------parametros-------
        self.ec = 1
        self.parametros(0,1)
        self.nombre = 'Paraboloide Hiperbólico'
        self.a = (float(self.txtA.get()) * float(self.txtA.get()))
        self.b = (float(self.txtB.get()) * float(self.txtB.get()))
        self.funcion = ('(',self.txtY.get(), '*Y*Y/', str(self.b), ')-(', 
                   self.txtX.get(), '*X*X/', str(self.a),')' )
        self.lblf = tkinter.Label(self.window, text=self.funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
    
        self.salir()
    #paraboloide_hiper
    
    def hiperboloide_doshojas(self): #LISTO 12 2
        self.portadadir = hiper2
        self.fondos(self.portadadir)
        self.ec = 2
        self.parametros(1,2)
        
        self.lblF = tkinter.Label(self.window, text="-1 = ", bg="black", fg ="white")
        self.lblF.place(x=350, y=432)
        
        self.nombre = 'Hiperboloide de dos Hojas'
        self.a = (float(self.txtA.get()) * float(self.txtA.get()))
        self.b = (float(self.txtB.get()) * float(self.txtB.get()))
        self.c = (float(self.txtC.get()) * float(self.txtC.get()))
        self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
                   self.txtY.get(), '*Y*Y/', str(self.b),')', '-(', self.txtZ.get(), '*Z*Z/',str(self.c),')' )
        self.lblf = tkinter.Label(self.window, text=self.funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        self.funcion2 = ('(',str(self.c),'*((',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
        self.txtY.get(), '*Y*Y/', str(self.b),')', '+1))**0.5' )
        
        self.salir()
    #hiperboloide_doshojas
    
    def elipsoide(self): #FALTAN PARAMETROS A,B,C 1,0
        self.portadadir = elipsoide
        self.fondos(self.portadadir)
        self.ec = 5
        #poner parametros
        self.parametros(1,0)
        
        self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                    command=self.btn_elip)
        self.graph.place(x=650, y=352, height = 50, width=75)
        
       
        self.salir()
    #elipsoide
    #####************************
    def btn_elip(self):
        
        ecuacion = self.ec
        self.gets(ecuacion)
        
        coefs = (float(self.txtA.get()), float(self.txtB.get()), float(self.txtC.get()))   
        rx, ry, rz = 1/np.sqrt(coefs) #LOS X SE MULTIPLICAN CON LOS PARAMETROS

        # angulos para los elipses
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        #ecuacion para elipsoides
        x = rx * np.outer(np.cos(u), np.sin(v))
        y = ry * np.outer(np.sin(u), np.sin(v))
        z = rz * np.outer(np.ones_like(u), np.cos(v))
        
        lFig = Figure(figsize=(5, 4), dpi=120)
        lAxis = Axes3D(lFig)
        lAxis.plot_surface(x, y, z,
                       rstride=1, cstride=1, 
                       cmap= self.colmap)
        # para el radio
        max_radius = max(rx, ry, rz)
        for axis in 'xyz':
            getattr(lAxis, 'set_{}lim'.format(axis))((-max_radius, max_radius))
        
        
        lWin = tkinter.Tk()
        lWin.title('Elipsoide')
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, 
                                    fill=tkinter.BOTH, expand=1)
        
    def paraboloide_eliptico(self): #LISTOOO 11 3
        self.portadadir = parel
        self.fondos(self.portadadir)
        self.ec = 3
        self.parametros(1,1)
        
        self.lblF = tkinter.Label(self.window, text="Z/C = ", bg="black", fg ="white")
        self.lblF.place(x=350, y=432)
        
        self.nombre = 'Paraboloide Eliptico'
        self.a = (float(self.txtA.get()) * float(self.txtA.get()))
        self.b = (float(self.txtB.get()) * float(self.txtB.get()))
        self.c = (float(self.txtC.get()) * float(self.txtC.get()))
        self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
                   self.txtY.get(), '*Y*Y/', str(self.b),')')
        self.lblf = tkinter.Label(self.window, text=self.funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        self.funcion2 = ('(',str(self.c),'*((',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
        self.txtY.get(), '*Y*Y/', str(self.b),')')
        
        self.salir()
    #paraboloide_eliptico
    
    def cilindro_hiperbolico(self): #
        self.portadadir = cilhip
        self.fondos(self.portadadir)
        self.nombre = 'Cilindro Hiperbolico'
        self.parametros(0,0)
        
        self.lblF = tkinter.Label(self.window, text="1 = ", bg="black", fg ="white")
        self.lblF.place(x=350, y=430)
        
        self.a = (float(self.txtA.get()) * float(self.txtA.get()))
        self.b = (float(self.txtB.get()) * float(self.txtB.get()))
        
        self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')-(', 
                   self.txtY.get(), '*Y*Y/', str(self.b),')')
        self.lblf = tkinter.Label(self.window, text=self.funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=352)
        #
        self.funcion2 = ('((',self.txtX.get(), '*X*X/5*',str(self.a),')-(',
        self.txtY.get(), '*2*Y*Y/4*', str(self.b),'))-1')
        
        self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                    command=self.btngraph5)
        self.graph.place(x=650, y=352, height = 50, width=75)
        
        self.salir()
    #cilindro_hiperbolico
    def btngraph5(self):
        self.a = (float(self.txtA.get()) * float(self.txtA.get()))
        self.b = (float(self.txtB.get()) * float(self.txtB.get()))
        self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')-(', 
                   self.txtY.get(), '*Y*Y/', str(self.b),')')
        self.funcion2 = ('((',self.txtX.get(), '*X*X/5*',str(self.a),')-(',
        self.txtY.get(), '*2*Y*Y/4*', str(self.b),'))-1')
        self.txtfunc = tkinter.Entry(self.window, borderwidth = 0, bg="black", fg ="black", width=5)
        self.txtfunc.place(x=980, y=352)
        prSetTxt(self.txtfunc, self.funcion2)
        
        self.lblf = tkinter.Label(self.window, text=self.funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        self.showPlot(self.txtfunc.get(), self.txtRi.get(),
                      self.txtRf.get(), self.txtstep.get(),1, 'Cilindro hiperbólico', self.colmap)
        
        
        
    def conoelip(self): #LISTOO 4
        self.portadadir = conoelip
        self.fondos(self.portadadir)
        self.ec = 4
        self.parametros(1,2)
        self.nombre = 'Cono Eliptico'
        self.lblF = tkinter.Label(self.window, text="Z/C = ", bg="black", fg ="white")
        self.lblF.place(x=350, y=432)
        
        self.nombre = 'Paraboloide Eliptico'
        self.a = (float(self.txtA.get()) * float(self.txtA.get()))
        self.b = (float(self.txtB.get()) * float(self.txtB.get()))
        self.c = (float(self.txtC.get()) * float(self.txtC.get()))
        self.funcion = ('(',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
                   self.txtY.get(), '*Y*Y/', str(self.b),')')
        self.lblf = tkinter.Label(self.window, text=self.funcion, bg="black", fg ="white")
        self.lblf.place(x=400, y=430)
        
        self.funcion2 = ('(',str(self.c),'*((',self.txtX.get(), '*X*X/', str(self.a), ')+(', 
        self.txtY.get(), '*Y*Y/', str(self.b),')', '))**0.5' )
        
        self.salir()
    #cono
    
    def historial(self):
        self.portadadir = historial
        self.fondos(self.portadadir)
        
        
        self.salir()
    #historial
#classPlotWin
    def txt(self):
        pass

class Historial():  #json (imagenes)
    pass

myPlotWin = PlotWin()
myPlotWin.createWindow()

Graficas = Graficador()
Graficas.showPlot()


