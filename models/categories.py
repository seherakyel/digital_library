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



def get_all_categories():
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query="SELECT * FROM digital_library.categories"
        cursor.execute(query,)
        return cursor.fetchall() 
    except Exception as e:
        print("kategori listelenmedi")
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(get_all_categories())



def get_categories_by_id(categoris_id):
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor()
        query="SELECT * FROM digital_library.categories WHERE id=%s"
        cursor.execute(query,(categoris_id,))
        return cursor.fetchall() 
    except Exception as e:
        print("kategori getirilemedi")
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(get_categories_by_id(1))


def add_categories(categories_name):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query="INSERT INTO categories(name) VALUES (%s)"
        cursor.execute(query,(categories_name,))
        connection.commit()
        print(f"{categories_name} eklendi")
    except Exception as e:
        print("kategori eklenmedi")
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()




def delete_categories_by_id(categories_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query="DELETE FROM categories WHERE id=%s"
        cursor.execute(query,(categories_id,))
        connection.commit()
        print(f"{categories_id} id'li kategori silindi")
    except Exception as e:
        print("kategori silinmedi")
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
print(delete_categories_by_id(2))

