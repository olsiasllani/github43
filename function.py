class Kursi:
    def _init_(self,emri,pershkrimi,projekti):
        self.emri = emri
        self.pershkrimi = pershkrimi
        self.projekti = projekti
        self.nxenesit = []

def regjistro_nxenes(self,nxenesi):
    """ Regjistron nje nxenes ne kurs."""
    self.nxenesit.append(nxenesi)
    print(f"{nxenesi.emri} eshte regjistruar ne kursin {self.emri}.")

def konrollo_perfundim_projekti(self,nxenesi):
    """ Kontrollon nese nxenesi ka perfunduar projektin dhe leshon certifikaten."""
    if nxenesi.projekti_perfunduar:
        print(f"Grate,{nxenesi.emri} ju keni marr certifikate per kursin {self.emri}.")
    else:
        f"{nxenesi.emri} nuk e ka perfunduar ende projektin per kursin
