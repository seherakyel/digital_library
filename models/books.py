
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



def add_books(title,author,description,category_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor()
        query="INSERT INTO books(title,author,description,category_id) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(title,author,description,category_id,))
        connection.commit()
        print("kitap basariyla eklendi.")
    finally:
        cursor.close()
        connection.close()




def get_book_by_id(books_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        query="SELECT * FROM digital_library.books WHERE id=%s"
        cursor.execute(query,(books_id,))
        results = cursor.fetchall()
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
        cursor.execute(query,(category_id))
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()
        connection.close()
print(get_books_by_category(2))




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
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query = "UPDATE books SET title = %s,author=%s,description=%s,cateogry_id=%s WHERE id = %s "
        cursor.execute(query, (title, author,description,category_id))
        connection.commit()
        print(f"{books_id} numarali kitap güncellendi.")
    finally:
        cursor.close()
        connection.close()
#print("")



def search_books_by_keyword(keyword): #dışarıdan bir keyword (anahtar kelime) alacak
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query="SELECT * FROM digital_library.books WHERE title LIKE %s OR author LIKE %s"
        search_value = f"%{keyword}%" # %kelime% → SQL’de bu, kelimenin hem başında hem sonunda her şey olabilir anlamına gelir
        cursor.execute(query, (search_value, search_value)) # İki tane %s vardı, o yüzden iki kez search_value gönderiyoruz (biri title, biri author için)
        results = cursor.fetchall()
        for book in results:
            print(book)
        return results
    finally:
        cursor.close()
        connection.close()
#print("insan")
