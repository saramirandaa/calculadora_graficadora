
def elipsoide(self):
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
    
    self.lblF = tkinter.Label(self.window, text="1 = ", bg="black", fg ="white")
    self.lblF.place(x=350, y=432)
    
    a = (float(self.txtA.get()) * float(self.txtA.get()))
    b = (float(self.txtB.get()) * float(self.txtB.get()))
    c = (float(self.txtC.get()) * float(self.txtC.get()))
    funcion = ('(',self.txtX.get(), '*X*X/', str(a), ')+(', 
               self.txtY.get(), '*Y*Y/', str(b),')', '+(', self.txtZ.get(), '*Z*Z/',str(c),')' )
    self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
    self.lblf.place(x=400, y=430)
    
    
    self.graph = tkinter.Button(self.window, borderwidth = 0, text = "GRAPH",
                                command=self.btngraph2)
    self.graph.place(x=650, y=352, height = 50, width=75)
    
    self.salir()
#elipsoide

def btngraph3(self):
    a = (float(self.txtA.get()) * float(self.txtA.get()))
    b = (float(self.txtB.get()) * float(self.txtB.get()))
    c = (float(self.txtC.get()) * float(self.txtC.get()))
    funcion = ('(',self.txtX.get(), '*X*X/', str(a), ')+(', 
    self.txtY.get(), '*Y*Y/', str(b),')', '+(', self.txtZ.get(), '*Z*Z/',str(c),')' )
   
    funcion2 = ('(',str(c),'*((',self.txtX.get(), '*X*X/', str(a), ')+(', 
    self.txtY.get(), '*Y*Y/', str(b),')', '+1))**0.5' )
    
    self.txtfunc = tkinter.Entry(self.window, borderwidth = 0, bg="black", fg ="black", width=5)
    self.txtfunc.place(x=980, y=430)
    prSetTxt(self.txtfunc, funcion2)
    
    self.lblf = tkinter.Label(self.window, text=funcion, bg="black", fg ="white")
    self.lblf.place(x=400, y=430)
    
    self.showPlot(self.txtfunc.get(), self.txtRi.get(),
                  self.txtRf.get(), self.txtstep.get(),1, 'Elipsoide')
#btngraph3
    