import sqlalchemy
from pprint import pprint
db = 'postgresql://muzicmen:12345678@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# 1 Количество исполнителей в каждом жанре
select_20 = connection.execute("""
    SELECT name_genre,COUNT(musician) FROM musicians
    JOIN genre_musician ON musicians.id = genre_musician.musician_id
    JOIN genres ON genre_musician.genres_id = genres.id
    GROUP BY name_genre;
    """).fetchall()
pprint(select_20)


# 2 количество треков, вошедших в альбомы 2019-2020 годов
select_21 = connection.execute("""
    SELECT year_of_release_album,COUNT(name_track) FROM albums a
    JOIN tracks t  ON a.id = t.album_id
    WHERE a.year_of_release_album  >= 2019 AND a.year_of_release_album <= 2020
    GROUP BY year_of_release_album;
    """).fetchall()
pprint(select_21)


#3  средняя продолжительность треков по каждому альбому;
select_22 = connection.execute("""
    SELECT name_album,AVG(duration) FROM albums a
    JOIN tracks t  ON a.id = t.album_id
    GROUP BY name_album;
    """).fetchall()
pprint(select_22)


#4 все исполнители, которые не выпустили альбомы в 2020 году;
select_22 = connection.execute("""
    SELECT musician,year_of_release_album FROM albums a
    JOIN musicians_albums ma  ON a.id = ma.album_id
    JOIN musicians m  ON ma.musician_id = m.id
    WHERE a.year_of_release_album != 2020;
    """).fetchall()
pprint(select_22)


#5 названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
select_23 = connection.execute("""
        SELECT name_digest FROM digests d
        JOIN composition_digest cd  ON d.id = cd.digest_id
        JOIN tracks t  ON cd.track_id = t.id
        JOIN albums a  ON t.album_id = a.id
        JOIN musicians_albums ma  ON a.id = ma.album_id
        JOIN musicians m  ON ma.musician_id = m.id
        WHERE m.musician LIKE 'Руки Вверх';
        """).fetchall()
pprint(select_23)


#6 название альбомов, в которых присутствуют исполнители более 1 жанра;
select_24 = connection.execute("""
        SELECT name_album FROM albums a
        JOIN musicians_albums ma  ON a.id = ma.album_id
        JOIN musicians m  ON ma.musician_id = m.id
        JOIN genre_musician gm  ON m.id = gm.musician_id
        GROUP BY m.musician, a.name_album
        HAVING count(gm.genres_id) > 1;
        """).fetchall()
pprint(select_24)


#7 наименование треков, которые не входят в сборники;
select_25 = connection.execute("""
        SELECT name_track FROM tracks t
        LEFT JOIN composition_digest cd ON t.id = cd.track_id
        WHERE cd.track_id IS NULL;
        """).fetchall()
pprint(select_25)


#8 исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
select_26 = connection.execute("""
        SELECT m.musician, t.duration FROM musicians m
        JOIN musicians_albums ma ON m.id = ma.musician_id
        JOIN albums a ON ma.album_id = a.id
        JOIN tracks t ON a.id = t.album_id
        WHERE t.duration IN (SELECT MIN(duration) FROM tracks)
        """).fetchall()
pprint(select_26)


#9 название альбомов, содержащих наименьшее количество треков.
select_27 = connection.execute('''
    SELECT a.name_album, COUNT(t.id) FROM albums a
    JOIN tracks t  ON a.id = t.album_id
    GROUP BY a.name_album 
    HAVING count(t.id) in (
        SELECT COUNT (t.id)
        FROM albums a
        JOIN tracks t  ON a.id = t.album_id
        GROUP BY a.name_album
        ORDER BY count(t.id)\
        LIMIT 1)
    ''').fetchall()
pprint(select_27)











