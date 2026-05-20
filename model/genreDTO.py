from dataclasses import dataclass


@dataclass
class GenreDTO:
    GenreId : int
    Name : str

    def __hash__(self):
        return hash(self.GenreId)

    def __str__(self):
        return self.Name

    def __eq__(self, other):
        if(self.GenreId==other.GenreId):
            return True
        else:
            return False
