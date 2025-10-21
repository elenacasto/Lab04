from CabinaStandard import CabinaStandard

class CabinaDeluxe(CabinaStandard):
    def __init__(self, codice, num_letti, ponte, prezzo, stile_deluxe):
        super().__init__(codice, num_letti, ponte, prezzo)
        self._stile_deluxe = stile_deluxe

    @property
    def prezzo(self):
        return self._prezzo * 1.20

    def __str__(self):
        stato = "Disponibile" if self._disponibile else "Occupata"
        return (f"{self._codice}: Deluxe | {self._num_letti} letti - Ponte {self._ponte} - "
                f"Prezzo - {self.prezzo} - Stile cabina: {self._stile_deluxe} - {stato}")


