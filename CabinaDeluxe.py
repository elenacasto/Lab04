class CabinaDeluxe:
    def __init__(self, codice, num_letti, ponte, prezzo, stile_deluxe):
        self._codice = codice
        self._num_letti = int(num_letti)
        self._ponte = int(ponte)
        self._prezzo = float(prezzo)
        self._stile_deluxe = stile_deluxe
        self._disponibile = True
        self._passeggero = None

    def prezzo(self):
        return self._prezzo * 1.20

    def __str__(self):
        stato = "Diposnibile" if self._disponibile else "Occupata"
        return f"{self._codice}: Deluxe | {self._num_letti} letti - Ponte {self._ponte} - Stile cabina: {self._stile_deluxe} - Disponibile"
