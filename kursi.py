# kursi.py

class Kursi :
    def __init__(self, emri, pershkrimi, projekti) :
        self.emri = emri
        self.pershkrimi = pershkrimi
        self.projekti = projekti
        self.nxenesit = []

    def regjistro_nxenes(self, nxenesi) :
        """Regjistron një nxënës në kurs."""
        self.nxenesit.append(nxenesi)
        print(f"{nxenesi.emri} është regjistruar në kursin {self.emri}.")

    def kontrollo_perfundimin_projekti(self, nxenesi) :
        """Kontrollon nëse nxënësi ka përfunduar projektin dhe lëshon certifikatën."""
        if nxenesi.projekti_perfunduar :
            print(f"Gratë, {nxenesi.emri}, ju keni marrë certifikatën për kursin {self.emri}!")
        else :
            print(f"{nxenesi.emri} nuk e ka përfunduar ende projektin për kursin {self.emri}.")
