"""
Aggregration is a specalized form of association with the whole and part relationships.

The whole and part are logically connnected through a container-contained heirarchy
The part can exists independently of the whole
The whole doesnt create or destroy part

Aggreagration is denoted with a solid line with a diamond diamond on the whole side.

"""

class Professor:

    def __init__(self, name:str, specialization:str) -> None:
        self.name = name
        self.specialization = specialization


class Department:

    def __init__(self, department_name:str, professors:list[Professor]) -> None:
        self.department_name = department_name
        self.professors = professors

    
    def add_professor(self, professor:Professor):
        self.professors.append(professor)
    
    def remove_professor(self, professor:Professor):
        self.professors.remove(professor)
    


professor1 = Professor('Sastry', 'Data Structures')
professor2 = Professor('Ratna Kumari', 'Compiler Design')
professor3 = Professor('harinadha', 'Algorithms')

professors = [professor1, professor2, professor3]


csDept = Department('CSE', professors=professors)


# Aggregation promoted reusability (payment microservices acorss different projects)
# Improved Flexibility
# Reflects real world relationship



# Music Library System


class Artist:

    def __init__(self, name:str) -> None:
        self.name = name


class Song:

    def __init__(self, name, artist:Artist, duration:int) -> None:
        self.name = name
        self.artist = artist
        self.duration = duration


class Library:

    def __init__(self) -> None:
        self.library = []

    def add_song(self, song) -> None:
        self.library.append(song)


class User:

    def __init__(self, name):
        self.name = name
        self.playlists = []

    
    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    def remove_playlist(self, playlist):
        self.playlists.remove(playlist)

class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, song):
        self.songs.remove(song)
    