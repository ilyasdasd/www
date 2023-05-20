import sqlalchemy
from pprint import pprint
db = 'postgresql://muzicmen:12345678@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# # Заполнение таблицы исполнителей
connection.execute("INSERT INTO musicians VALUES ( 1,'Сектор Газа','Юрий Хой');")
connection.execute("INSERT INTO musicians VALUES ( 2,'Михаил Круг','Миха');")
connection.execute("INSERT INTO musicians VALUES ( 3,'Руки Вверх','Сергей Жуков');")
connection.execute("INSERT INTO musicians VALUES ( 4,'Золотое кольцо','Надежда Кадышева');")
connection.execute("INSERT INTO musicians VALUES ( 5,'Snoop Dogg','Snoop');")
connection.execute("INSERT INTO musicians VALUES ( 6,'Тимати','Тиму́р Ильда́рович Юну́сов ');")
connection.execute("INSERT INTO musicians VALUES ( 7,'Егор Крид','Его́р Никола́евич Була́ткин ');")
connection.execute("INSERT INTO musicians VALUES ( 8,'AC/DC','братья Малькольмы и Ангус Янгам');")


# # Заполнение таблицы жанров
connection.execute("INSERT INTO genres VALUES ( 1,'Шансон');")
connection.execute("INSERT INTO genres VALUES ( 2,'Рок');")
connection.execute("INSERT INTO genres VALUES ( 3,'Народные песни');")
connection.execute("INSERT INTO genres VALUES ( 4,'ПОП-музыка');")
connection.execute("INSERT INTO genres VALUES ( 5,'Рэп');")


# Заполнение таблицы жанров музыкантов(genre_musician)
connection.execute("INSERT INTO genre_musician VALUES ( 1,1,2);")
connection.execute("INSERT INTO genre_musician VALUES ( 2,2,1);")
connection.execute("INSERT INTO genre_musician VALUES ( 6,2,8);")
connection.execute("INSERT INTO genre_musician VALUES ( 3,3,4);")
connection.execute("INSERT INTO genre_musician VALUES ( 4,4,3);")
connection.execute("INSERT INTO genre_musician VALUES ( 7,4,7);")
connection.execute("INSERT INTO genre_musician VALUES ( 5,5,6);")
connection.execute("INSERT INTO genre_musician VALUES ( 8,5,5);")


# Заполнение таблицы альбомов
connection.execute("INSERT INTO albums VALUES ( 1,'Колхозный панк',1991);")
connection.execute("INSERT INTO albums VALUES ( 2,'Жиган-лимон',1994);")
connection.execute("INSERT INTO albums VALUES ( 3,'Маленькие девочки',2001);")
connection.execute("INSERT INTO albums VALUES ( 4,'Течёт ручей',1995);")
connection.execute("INSERT INTO albums VALUES ( 5,'No Limit Top Dogg',1999);")
connection.execute("INSERT INTO albums VALUES ( 6,'Black Star',2020);")
connection.execute("INSERT INTO albums VALUES ( 7,'Холостяк',2019);")
connection.execute("INSERT INTO albums VALUES ( 8,'Back in Black',1980);")


# # Заполнение таблицы треков
connection.execute("""INSERT INTO tracks VALUES ( 1,'Колхозный панк', '2.38', 1);""")
connection.execute("""INSERT INTO tracks VALUES ( 2,'Местные','3.50',1);""")
connection.execute("""INSERT INTO tracks VALUES ( 3,'А сечку жрите сами','2.59',2);""")
connection.execute("""INSERT INTO tracks VALUES ( 4,'Девочка — пай','2.49',2);""")
connection.execute("""INSERT INTO tracks VALUES ( 5,'18 Мне Уже','4.07',3);""")
connection.execute("""INSERT INTO tracks VALUES ( 6,'мой сынок','3.50',3);""")
connection.execute("""INSERT INTO tracks VALUES ( 7,'Течёт ручей','3.01',4);""")
connection.execute("""INSERT INTO tracks VALUES ( 8,'Buck Em','2.44',5);""")
connection.execute("""INSERT INTO tracks VALUES ( 9,'Bitch Please','3.54',5);""")
connection.execute("""INSERT INTO tracks VALUES ( 10,'В Клубе','4.25',6);""")
connection.execute("""INSERT INTO tracks VALUES ( 11,'Я и Ты','4.44',6);""")
connection.execute("""INSERT INTO tracks VALUES ( 12,'Самая самая','3.50',7);""")
connection.execute("""INSERT INTO tracks VALUES ( 13,'Ревность','3.18',7);""")
connection.execute("""INSERT INTO tracks VALUES ( 14,'Hells Bells','5.12',8);""")
connection.execute("""INSERT INTO tracks VALUES ( 15,'Back in Black','4.15',8);""")
connection.execute("""INSERT INTO tracks VALUES ( 16,'Back','4.1',8);""")


# # Заполнение таблицы сборники
connection.execute("INSERT INTO digests VALUES ( 1,'Лучшие песни Сектор-Газа',2005);")
connection.execute("INSERT INTO digests VALUES ( 2,'Лучшие песни М.Круга',2010);")
connection.execute("INSERT INTO digests VALUES ( 3,'Лучшие песни Руки Вверх',2018);")
connection.execute("INSERT INTO digests VALUES ( 4,'Песни Надежды Кадышевой',1995);")
connection.execute("INSERT INTO digests VALUES ( 5,'Лучшие песни Snoop DOgg',2020);")
connection.execute("INSERT INTO digests VALUES ( 6,'Тимати-Лучшии из',2013);")
connection.execute("INSERT INTO digests VALUES ( 7,'Лучшие песни Крида',2021);")
connection.execute("INSERT INTO digests VALUES ( 8,'AC/DC лучшие на все времена',2001);")


#  Заполнение таблицы состав сборника(composition_digest)
connection.execute("INSERT INTO composition_digest VALUES ( 1,1,1);")
connection.execute("INSERT INTO composition_digest VALUES ( 2,1,2);")
connection.execute("INSERT INTO composition_digest VALUES ( 3,2,3);")
connection.execute("INSERT INTO composition_digest VALUES ( 4,2,4);")
connection.execute("INSERT INTO composition_digest VALUES ( 5,3,5);")
connection.execute("INSERT INTO composition_digest VALUES ( 6,3,6);")
connection.execute("INSERT INTO composition_digest VALUES ( 7,4,7);")
connection.execute("INSERT INTO composition_digest VALUES ( 8,5,8);")
connection.execute("INSERT INTO composition_digest VALUES ( 9,5,9);")
connection.execute("INSERT INTO composition_digest VALUES ( 10,6,10);")
connection.execute("INSERT INTO composition_digest VALUES ( 11,6,11);")
connection.execute("INSERT INTO composition_digest VALUES ( 12,7,12);")
connection.execute("INSERT INTO composition_digest VALUES ( 13,7,13);")
connection.execute("INSERT INTO composition_digest VALUES ( 14,8,14);")
connection.execute("INSERT INTO composition_digest VALUES ( 15,8,15);")



# # Заполнение таблицы альбомы исполнителей
connection.execute("INSERT INTO musicians_albums VALUES ( 1,1,1);")
connection.execute("INSERT INTO musicians_albums VALUES ( 2,2,2);")
connection.execute("INSERT INTO musicians_albums VALUES ( 3,3,3);")
connection.execute("INSERT INTO musicians_albums VALUES ( 4,4,4);")
connection.execute("INSERT INTO musicians_albums VALUES ( 5,5,5);")
connection.execute("INSERT INTO musicians_albums VALUES ( 6,6,6);")
connection.execute("INSERT INTO musicians_albums VALUES ( 7,7,7);")
connection.execute("INSERT INTO musicians_albums VALUES ( 8,8,8);")
connection.execute("INSERT INTO musicians_albums VALUES ( 9,8,8);")









