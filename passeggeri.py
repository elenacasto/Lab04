class Passeggeri:
    def __init__(self, codice_passeggero, nome_passeggero, cognome):
        self._codice_passeggero = codice_passeggero
        self._nome_passeggero = nome_passeggero
        self._cognome = cognome
        self._cabina = None

    @property
    def codice_passeggero(self):
        return self._codice_passeggero

    @property
    def cabina(self):
        return self._cabina

    @cabina.setter
    def cabina(self, cabina):
        self._cabina = cabina

    def __str__(self):
        cabina = self.cabina.codice if self.cabina else "Nessuna cabina assegnata"
        return f"{self._codice_passeggero}: {self._nome_passeggero} {self._cognome} - Cabina: {cabina}"