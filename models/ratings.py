
from multiprocessing import connection
import mysql.connector
from mysql.connector import Error

CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789',
    'database': 'digital_library'
}
def is_db_connected():
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        print("baglanti basarisiz")
    else:
        print("baglanti basarili")
is_db_connected()




def add_rating(user_id, book_id, rating, comment):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query = "INSERT INTO ratings(user_id, book_id, rating, comment) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user_id, book_id, rating, comment))
        connection.commit()
        print("Puan ve yorum başarıyla eklendi.")
    finally:
        cursor.close()
        connection.close()
#print(add_rating(1, 2, 5, "Harika bir kitap!"))


def get_ratings_by_book_id(book_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM ratings WHERE book_id = %s"
        cursor.execute(query, (book_id,))
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()
        connection.close()
#print(get_ratings_by_book_id(2))


def get_average_rating_for_book(book_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query = "SELECT AVG(rating) FROM ratings WHERE book_id = %s" # AVG → “average” yani ortalama anlamına gelir
        cursor.execute(query, (book_id,))
        avg_rating = cursor.fetchone()[0]
        return avg_rating
    finally:
        cursor.close()
        connection.close()
#print(get_average_rating_for_book(2))


def get_user_rating_for_book(user_id, book_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM ratings WHERE user_id = %s AND book_id = %s"
        cursor.execute(query, (user_id, book_id))
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        connection.close()
#print(get_user_rating_for_book(1, 2))
