
from multiprocessing import connection
import mysql.connector
from mysql.connector import Error

CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789',
    'database': 'food_choice'
}
def is_db_connected():
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        print("baglanti basarisiz")
    else:
        print("baglanti basarili")
is_db_connected()



def add_books(title,author,description,category_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor()
        query="INSERT INTO books(title,author,description,category_id) VALUES (%s,%s,%s,%s)"
        cursor.execute(query(title,author,description,category_id))
        connection.commit()
        print("kitap basariyla eklendi.")
    finally:
        cursor.close()
        connection.close()
print(add_books("a","b","cdf",3))




def get_book_by_id(books_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        query="SELECT * FROM digital_library.books WHERE id=%s"
        results = cursor.fetchall()
        for books in results:
            print(books)
        return results
    finally:
        cursor.close()
        connection.close()
#print(get_book_by_id(1))




def get_all_books():
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return  None
    try:
        cursor=connection.cursor(dictionary=True)
        query="SELECT * FROM digital_library.books "
        cursor.execute(query,)
        book=cursor.fetchall()
        return book
    except Exception as e:
        print("kitap listlenmedi") 
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(get_all_books())  




def get_books_by_category(category_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query="SELECT * FROM digital_library.books WHERE cateogry_id=%s"
        results = cursor.fetchall()
        for books in results:
            print(books)
        return results
    finally:
        cursor.close()
        connection.close()



def delete_books_by_id(books_id):
    connection = mysql.connector.connect(**CONFIG)
    try:
        cursor = connection.cursor()
        query = "DELETE FROM books WHERE id = %s"
        cursor.execute(query, (books_id,))
        connection.commit()
        print(f"{books_id} numarali kitap silindi.")
    finally:
        cursor.close()
        connection.close()
#print(delete_books_by_id(1))



def update_books(books_id, title, author,description,category_id):
    connection = mysql.connector.connect(**CONFIG)
    try:
        cursor = connection.cursor()
        query = "UPDATE books SET title = %s,author=%s,description=%s,cateogry_id=%s WHERE id = %s "
        cursor.execute(query, (title, author,description,category_id))
        connection.commit()
        print(f"{books_id} numarali kitap güncellendi.")
    finally:
        cursor.close()
        connection.close()


