class Libri:
    def __init__(self, titulli, autori, vitin_publikimit):
    self.titulli = titulli
    self.autori = autori
    self.vitin_publikimit = vitin_publikimit
    
    
    def informacion(self):
        return f"{self.titulli} nga {self.autori}, botuar nr vitin {self.vitin_publikimit}"
    
    class Bibloteka:
        def __init__(self):
            self.librat = []
            
     def shto_liber(self, liber):
         self.librat.append(liber)
         
 def shfaq_librat(self):
     for liber in self.librat: 
         print(liber.informacion())
         
         
libri1 = Libri("1984", "George Orwell", 1949)
libri2 = Libri("To Kill a Mockinbird", "Harper Lee", 1960)

bibloteka = Bibloteka()

bibloteka.shto_liber(libri1)
bibloteka.shto_liber(libri2)

bibloteka.shfaq_librat()
