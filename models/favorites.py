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


def add_favorites_book(user_id, book_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return True
    try:
        cursor = connection.cursor(dictionary=True)
        # once kontrol et
        check_query = "SELECT * FROM favorites WHERE user_id = %s AND book_id = %s"
        cursor.execute(check_query, (user_id, book_id))
        existing = cursor.fetchone()
        if existing:
            print(f"Kullanıcı {user_id}, kitap {book_id} zaten favorilere eklemiş")
            return None
        # yoksa ekle
        insert_query = "INSERT INTO favorites (user_id, book_id) VALUES (%s, %s)"
        cursor.execute(insert_query, (user_id, book_id))
        connection.commit()
        print(f"Kullanıcı {user_id}, kitap {book_id}'i favorilere ekledi")
    except Exception as e:
        print("Favorilere eklenmedi")
        print(f"hata: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(add_favorites_book(1,2))


def get_favorites_by_user_id(user_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query="SELECT * FROM digital_library.favorites WHERE id=%s"
        cursor.execute(query,(user_id,))
        return cursor.fetchall() 
    except Exception as e:
        print("kullanici favorileri getirilemedi")
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(get_favorites_by_user_id(2))



def all_book_favorites_by_user(user_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query="SELECT * FROM digital_library.favorites  WHERE id=%s "
        cursor.execute(query,(user_id,))
        favori=cursor.fetchall()
        return favori
    except Exception as e:
        print("kullanici favori listlenmedi") 
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(all_book_favorited_by_user(2))





def remove_favorites_book(user_id,book_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query = "DELETE FROM favorites WHERE user_id = %s AND book_id = %s"
        cursor.execute(query, (user_id, book_id))
        connection.commit()
        print(f"Kullanıcı {user_id}, kitap {book_id} favorilerden kaldırıldı.")
    finally:
        cursor.close()
        connection.close()
#print(remove_favorites_book(1, 2))
