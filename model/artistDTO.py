from dataclasses import dataclass


@dataclass
class ArtistDTO:
    ArtistId : int
    Name : str

    def __hash__(self):
        return hash(self.ArtistId)

    def __str__(self):
        return self.Name

    def __eq__(self, other):
        if (self.ArtistId==other.ArtistId):
            return True
        else:
            return False
