import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):

        self.grafo = nx.DiGraph()

        self.idMap = {}
        for artista in DAO.getTuttiArtisti():
            self.idMap[artista.ArtistId] = artista

    def getGeneri(self):
        generi = DAO.getGenre()
        return generi

    def craGrafo(self, GenreId):

        self.grafo.clear()

        id_nodi = DAO.getNodi(GenreId)

        for id in id_nodi:
            art = self.idMap[id]
            self.grafo.add_node(art)

        for id1, id2 in DAO.getArchi(GenreId):
            a1 = self.idMap[id1]
            a2 = self.idMap[id2]

            p1 = DAO.popolarita(id1,GenreId)
            p2 = DAO.popolarita(id2,GenreId)

            if p1 > p2:
                self.grafo.add_edge(a1, a2, weight=(p1 + p2))
            if p2 > p1:
                self.grafo.add_edge(a2, a1, weight=(p1 + p2))
            if p1 == p2:
                self.grafo.add_edge(a1, a2, weight=(p1 + p2))
                self.grafo.add_edge(a2, a1, weight=(p1 + p2))

        return len(list(self.grafo.nodes)), len(list(self.grafo.edges))

    def best5archi(self):
        archi_ordinati = sorted(self.grafo.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)

        s=""
        i=0

        for arco in archi_ordinati:
            if i < 5:
                s = s +str(arco[0]) +" --> "+str(arco[1])+" " + str(arco[2]['weight'])+"\n"
            i=i+1

        return s



