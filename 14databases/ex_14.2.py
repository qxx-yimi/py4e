import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


fname = input('Enter file name: ')
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

for entry in all:
    if lookup(entry, 'Track ID') is None:
        continue

    track_title = lookup(entry, 'Name')
    track_len = lookup(entry, 'Total Time')
    track_rating = lookup(entry, 'Rating')
    track_count = lookup(entry, 'Play Count')
    artist_name = lookup(entry, 'Artist')
    genre_name = lookup(entry, 'Genre')
    album_title = lookup(entry, 'Album')

    if genre_name is None or artist_name is None or album_title is None or track_title is None:
        continue

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist_name,))
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre_name, ))

    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist_name,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES ( ?, ? )', (artist_id, album_title))

    cur.execute('SELECT id FROM Album WHERE title = ? ', (album_title,))
    album_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, 
    ?, ? )''', (track_title, album_id, genre_id, track_len, track_rating, track_count))

conn.commit()
