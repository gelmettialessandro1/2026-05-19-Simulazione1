from database.DB_connect import DBConnect
from model.genreDTO import GenreDTO
from model.artistDTO import ArtistDTO


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getGenre():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""select * 
                            from genre
                            """)

        lista = cursor.fetchall()

        risultati = []

        for diz in lista:
            risultati.append(GenreDTO(diz["GenreId"], diz["Name"]))

        cursor.close()
        cnx.close()

        return risultati

    @staticmethod
    def getTuttiArtisti():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""select * 
                        from artist
                                """)

        lista = cursor.fetchall()

        risultati = []

        for diz in lista:
            risultati.append(ArtistDTO(diz["ArtistId"], diz["Name"]))

        cursor.close()
        cnx.close()

        return risultati


    @staticmethod
    def getNodi(GenreId):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""select distinct art.artistId as ID
                        from artist art , track t , album alb
                        where t.AlbumId  = alb.AlbumId and art.ArtistId = alb.ArtistId and t.GenreId = %s
                                    """, (GenreId,))

        lista = cursor.fetchall()

        risultati = []

        for diz in lista:
            risultati.append(diz["ID"])

        cursor.close()
        cnx.close()

        return risultati





    @staticmethod
    def getArchi(GenreId):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""select distinct tab1.a1 id1, tab2.a2 id2
                        from 
                        (select i.CustomerId c2, a.ArtistId a1
                        from invoice i, invoiceline il, track t , album a 
                        where t.GenreId = %s and i.InvoiceId = il.InvoiceId and il.TrackId = t.TrackId and t.AlbumId = a.AlbumId ) tab1 
                        ,
                        (select i.CustomerId c1 , a.ArtistId a2
                        from invoice i, invoiceline il, track t , album a 
                        where t.GenreId = %s and i.InvoiceId = il.InvoiceId and il.TrackId = t.TrackId and t.AlbumId = a.AlbumId ) tab2
                        
                        where c1 = c2 and a1<a2 """, (GenreId, GenreId))

        lista = cursor.fetchall()

        risultati = []

        for diz in lista:
            risultati.append((diz["id1"],diz["id2"]))

        cursor.close()
        cnx.close()

        return risultati

    @staticmethod
    def popolarita(ArtistId, GenreId):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        cursor.execute("""select sum(il.Quantity) as q
from invoiceline il, track t, album a
where il.TrackId = t.TrackId and t.AlbumId = a.AlbumId and a.ArtistId = %s and t.GenreId = %s """,
                       (ArtistId, GenreId))

        lista = cursor.fetchall()



        cursor.close()
        cnx.close()

        for diz in lista:
            return int(diz["q"])







