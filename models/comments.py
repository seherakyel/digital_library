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



def add_comments(user_id,book_id,content):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query = "INSERT INTO comments (user_id, book_id,content) VALUES (%s, %s,%s)"
        cursor.execute(query, (user_id, book_id,content,))
        connection.commit()
        print(f"Kullanıcı {user_id}, kitap {book_id}'i ,yorum {content} ekledi")
    except Exception as e:
        print("yorum eklenmedi")
        print(f"hata: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(add_comments(1,2,"ajhdha"))
    
def get_comments_by_book_id(book_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM comments WHERE book_id = %s"
        cursor.execute(query, (book_id,))
        results = cursor.fetchall()
        print(f"Kitap {book_id} için bulunan yorumlar:")
        for comment in results:
            print(comment)
        return results
    except Exception as e:
        print("Yorumlar getirilemedi")
        print(f"hata: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(get_comments_by_book_id(2))



def delete_comment(comment_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query = "DELETE FROM comments WHERE id = %s"
        cursor.execute(query, (comment_id,))
        connection.commit()
        print(f"{comment_id} numaralı yorum başarıyla silindi.")
    except Exception as e:
        print("Yorum silinemedi")
        print(f"hata: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(delete_comment(1))



def get_comment_count_for_book(book_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM comments WHERE book_id = %s"
        cursor.execute(query, (book_id,))
        count = cursor.fetchone()[0]
        print(f"Kitap {book_id} için toplam yorum sayısı: {count}")
        return count
    except Exception as e:
        print("Yorum sayısı getirilemedi")
        print(f"hata: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(get_comment_count_for_book(2))







