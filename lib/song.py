from . import CURSOR

class Song:
    pass
    def __init__(self, name, album):
        pass
        self.id = None
        self.name = name
        self.album = album
        
        
    @classmethod
    def create(cls, name, album):
        pass
        song = Song(name, album)
        song.save()
        return song
    
    @classmethod
    def create_table(self):
        pass
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        
        CURSOR.execute(sql)

    def save(self):
        pass
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        
        CURSOR.execute(sql, (self.name, self.album))
        
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]