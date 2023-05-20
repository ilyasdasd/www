import sqlalchemy
from pprint import pprint
db = 'postgresql://muzicmen:12345678@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# 1 Название и год выхода альбомов,вышедших в 2018 году
select_1 = connection.execute("SELECT name_album,year_of_release_album FROM albums "
                        "WHERE year_of_release_album=2018;").fetchall()
pprint(select_1)

# 2 Название и продолжительность самого длительного трека
select_2 = connection.execute("SELECT name_track,duration FROM tracks "
                        "WHERE duration=(SELECT MAX(duration) FROM tracks);").fetchall()
pprint(select_2)

# 3 Название треков, продолжительность которых не менее 3,5 минуты
select_3 = connection.execute("SELECT name_track,duration FROM tracks "
                        "WHERE duration >= 3.5;").fetchall()
pprint(select_3)

#4 Названия сборников, вышедших в период с 2018 по 2020 год включительно
select_4 = connection.execute("SELECT name_digest,year_of_release_digest FROM digests "
                        "WHERE  year_of_release_digest BETWEEN 2018 AND 2020;").fetchall()
pprint(select_4)

# 5 Исполнители, чье имя состоит из 1 слова
select_5 = connection.execute("SELECT musician FROM musicians "
                        "WHERE musician NOT LIKE '%% %%' ;").fetchall()
pprint(select_5)


# 6 Название треков, которые содержат слово "мой"/"my"
select_6 = connection.execute("SELECT name_track FROM tracks "
                              "WHERE name_track LIKE '%%мой%%';").fetchall()
pprint(select_6)















