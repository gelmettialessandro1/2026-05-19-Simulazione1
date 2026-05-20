import flet as ft
from model.genreDTO import GenreDTO

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenre(self):
        generi = self._model.getGeneri()

        for genere in generi:
            self._view._ddGenre.options.append(ft.dropdown.Option(key=genere.GenreId, text=str(genere)))

        self._view.update_page()

    def handleCreaGrafo(self, e):
        if self._view._ddGenre.value == None:
            self._view.txt_result.controls.append(ft.Text("non hai selezionato genere"))
            self._view.update_page()
            return

        GenreId = int(self._view._ddGenre.value)

        nodi,archi =self._model.craGrafo(GenreId)
        self._view.txt_result.controls.append(ft.Text(f"numero nodi{nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"numero achi{archi}"))
        self._view.txt_result.controls.append(ft.Text(f"best 5 archi:\n{self._model.best5archi()}"))
        self._view.update_page()




    def handleCammino(self,e):
        pass