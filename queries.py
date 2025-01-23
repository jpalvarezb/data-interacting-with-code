# pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')

def directors_count(db):
    # return the total number of directors
    db = conn.cursor()
    query = 'SELECT COUNT(directors.id)\
            FROM directors'
    db.execute(query)
    count = db.fetchall()
    result = count[0][0]
    return result

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    db = conn.cursor()
    query = 'SELECT directors.name\
        FROM directors\
        ORDER BY name ASC'
    db.execute(query)
    directors = db.fetchall()
    result = []
    for director in directors:
        result.append(director[0])
    return result


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    db = conn.cursor()
    query = 'SELECT movies.title AS titles\
    FROM movies\
    WHERE UPPER(titles) LIKE "% LOVE"\
    OR UPPER(titles) LIKE "LOVE %"\
    OR UPPER(titles) LIKE "% LOVE %"\
    OR UPPER(titles) LIKE "LOVE"\
    OR UPPER(titles) LIKE "% LOVE\'%"\
    OR UPPER(titles) LIKE "% LOVE."\
    OR UPPER(titles) LIKE "LOVE,%"\
    ORDER BY titles ASC'
    db.execute(query)
    titles = db.fetchall()
    result = []
    for title in titles:
        result.append(title[0])
    return result


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    db = conn.cursor()
    sql_name = f'%{name}%'
    query = "SELECT COUNT(directors.id)\
    FROM directors\
    WHERE UPPER(directors.name) LIKE ?"
    db.execute(query, (sql_name.upper(),))
    count = db.fetchone()
    result = count[0]
    return result


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    db = conn.cursor()
    query = "SELECT movies.title\
    FROM movies\
    WHERE movies.minutes > ?\
    ORDER BY movies.title ASC"
    db.execute(query, (min_length,))
    movies = db.fetchall()
    result = []
    for movie in movies:
        result.append(movie[0])
    return result
