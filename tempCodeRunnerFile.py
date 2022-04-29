
        pass
    #botones
    
    def fondos(self, ruta):
        self.portada = Image.open(ruta)
        self.test = ImageTk.PhotoImage(self.portada)