from CabinaStandard import CabinaStandard
from CabinaAnimali import CabinaAnimali
from CabinaDeluxe import CabinaDeluxe

from passeggeri import Passeggeri

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self._cabina = []
        self._passeggeri = []

    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip().split(",")

                if line[0].startswith("CAB"):
                    codice = line[0]
                    num_letti = int(line[1])
                    ponte = int(line[2])
                    prezzo = float(line[3])

                    if len(line) == 4:
                        cabina = CabinaStandard(codice, num_letti, ponte, prezzo)
                    elif line[4].isdigit():
                        max_animali = int(line[4])
                        cabina = CabinaAnimali(codice, num_letti, ponte, prezzo, max_animali)
                    else :
                        stile_deluxe = line[4]
                        cabina = CabinaDeluxe(codice, num_letti, ponte, prezzo, stile_deluxe)

                    self._cabina.append(cabina)

                elif line[0].startswith("P"):
                    codice_passeggero = line[0]
                    nome_passeggero = line[1]
                    cognome = line[2]

                    self._passeggeri.append(Passeggeri(codice_passeggero, nome_passeggero, cognome))


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        cabina = next((c for c in self._cabina if c.codice == codice_cabina), None)
        passeggero = next((p for p in self._passeggeri if p.codice_passeggero == codice_passeggero), None)

        if cabina is None:
            print("Cabina non esistente")
            return
        if passeggero is None:
            print("Passeggero non esistente")
            return
        if not cabina.disponibile:
            print("Cabina non disponibile")
            return
        if passeggero.cabina is not None:
            print("Passeggero già assegnato a una cabina")
            return

        cabina.assegna_passeggero(passeggero)
        passeggero.cabina = cabina


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self._cabina, key=lambda c: c.prezzo)

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self._passeggeri:
            cabina_info = f"Cabina: {passeggero.cabina.codice}" if passeggero.cabina else "Nessuna cabina assegnata"
            print(f"{passeggero.codice_passeggero}: {passeggero.nome} {passeggero.cognome}, {cabina_info}")
