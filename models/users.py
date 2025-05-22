
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


#add_users(user_name,mail,password,is_active)
#delete_users_by_id(users_id)
#update_users(users_id,user_name,email,password,is_active)
#is_active()
#Users_login(email,password)
#Register_user(user_name,mail,password)

def get_users_full_info_by_id(users_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query="SELECT * FROM digital_library.users WHERE id=%s"
        cursor.execute(query,(users_id,))  
        user=cursor.fetchone()
        return user
    
    except Exception as e:
        print("kullanici getirelemedi")
        print(f"hata:{e}")
        return 
    finally:
        cursor.close()
        connection.close()
#print(get_users_full_info_by_id(1))



def get_users_by_user_name(users_name):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query="SELECT user_name FROM digital_library.users WHERE user_name=%s"
        cursor.execute(query,(users_name,))  
        users=cursor.fetchone()
        return users
    
    except Exception as e:
        print("kullanici getirilemedi")
        print(f"hata:{e}")
        return None
    
    finally:
        cursor.close()
        connection.close()
#print(get_users_by_user_name("elif"))



def delete_users_by_id(users_id):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query="DELETE FROM digital_library.users WHERE id=%s"
        cursor.execute(query,(users_id,))
        connection.commit()
        print(f"{users_id} id'li kullanici silindi")
    except Exception as e:
        print("kullanici silinemedi")
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(delete_users_by_id(2))