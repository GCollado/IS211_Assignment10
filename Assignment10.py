from sqlite3 import Error
import sqlite3

"""
Part 1 Music Database
 Create a relational database model containing the music artist, album, song, and song length.
1) Create the Artist, Album, and Songs tables.
    a. The Artist table has the artist name.
    b. The Album table has the artist name and album title.
    c. The Songs Table has the song title, album, track number and song length.
2) Create relational tables to link the relevant information
3. Submit a file named "music.sql" with SQL CREATE queries
"""
def establish_connection():
    #Creates con database in Memory
    try:
        con = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    return con

def create_artist_table(con):
    cursor = con.cursor()
    #Createst artists table if it does not exists
    cursor.execute("""CREATE TABLE IF NOT EXISTS artists(artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_name TEXT UNIQUE)""")

def create_album_table(con):
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS albums(album_id INTEGER PRIMARY KEY AUTOINCREMENT,
     album_title TEXT UNIQUE,
      album_artist INTEGER,
       FOREIGN KEY(album_artist)
        REFERENCES artists(artist_id))""")

def create_songs_table(con):
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS songs(song_id INTEGER PRIMARY KEY AUTOINCREMENT,
     song_title TEXT, album_title INTEGER, track_number INTEGER, song_length INTEGER,
      FOREIGN KEY(album_title) REFERENCES albums(album_id))""")

def insert_artist_name(con):
    cursor = con.cursor()
    #Inserts artists name to artist table
    cursor.execute("""INSERT INTO artists(artist_name) VALUES('Nirvana')""")
    cursor.execute("""INSERT INTO artists(artist_name) VALUES('Queens of the Stone Age')""")

def insert_album_title(con):
    cursor = con.cursor()
    #Inserts artists name to album table
    cursor.execute("""INSERT INTO albums(album_title, album_artist) VALUES('Nevermind', '1')""")
    cursor.execute("""INSERT INTO albums(album_title, album_artist)
     VALUES('Lullabies to Paralyze', '2')""")


def insert_song_title(con):
    cursor = con.cursor()
    #Inserts artists name to song table
    cursor.execute("""INSERT INTO songs(song_title) VALUES('Lithium')""")
    cursor.execute("""INSERT INTO songs(song_title) VALUES('Little Sister')""")

def select_all_artists(con):
    cursor = con.cursor()
    #cursor.execute("""SELECT * FROM artists""")
#    cursor.execute("""SELECT * FROM artists JOIN albums""")
    cursor.execute("""SELECT artists.artist_name, albums.album_title FROM artists INNER JOIN albums ON albums.album_artist = artists.artist_id""")

    #cursor.execute("""SELECT * FROM albums""")

    rows = cursor.fetchall()
    print("|      Artist            |    album name    |".format())
    for row in rows:
        print('  {}  |  {}  '.format(row[0], row[1]))


def run_sql_file():
    fd = open('music.sql', 'r')
    script = fd.read()
    c.executescript(script)
    fd.close()

def main():
    conn = establish_connection()
    with conn:
        create_artist_table(conn)
        create_album_table(conn)
        create_songs_table(conn)

        insert_artist_name(conn)
        insert_album_title(conn)
        insert_song_title(conn)

        select_all_artists(conn)

#close the connection
#con.close()

if __name__ == '__main__':
    main()


