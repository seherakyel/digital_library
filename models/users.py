
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



# ömere sor 
def update_users(users_id,user_name,email,password,is_active):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query = """
            UPDATE digital_library.users
            SET user_name = %s,email=%s,password=%s,is_active=%s
            WHERE id = %s
        """
        cursor.execute(query,(user_name,email,password,is_active,users_id))
        connection.commit()
        print(f"{user_name} kullanisi güncellendi")

    except Exception as e:
        print("kullanici güncellenemedi")
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(update_users("a","b.@mail.com","123",1,3))




def is_active(users_id):
    connection = mysql.connector.connect(**CONFIG) 
    if not connection: 
        return None
    try: 
        cursor=connection.cursor(dictionary=True)
        query="SELECT * FROM digital_library.users WHERE id=%s"
        cursor.execute(query,(users_id,))  
        users=cursor.fetchone()

        if users and users["is_active"] == 1:
            print("kullanici aktif")
        else:
            print("kullanici aktif degildir")

    except Exception as e:
        print(f"hata:{e}")
        return None
    finally:
        cursor.close()
        connection.close()
#print(is_active(3))



def Users_login(email,password):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query = "SELECT * FROM digital_library.users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchall()
        if result:
            Users=result[0]
            print(f"giris basarili:hos geldin {Users['email']}")
            return Users
        else:
            print("hatali kullanici adi veya şifre")
            return None
    except mysql.connector.Error as db_err:
            print(f"Veritabanı işlem hatası: {db_err}")
            return None
    except mysql.connector.Error as conn_err:
            print(f"Veritabanı bağlantı hatası: {conn_err}")
            return None
    except Exception as e:
            print(f"Beklenmeyen hata: {e}")
            return None
    finally:
        cursor.close()
        connection.close()
#print(Users_login("elif@mail.com","hashed_password3"))




def Register_users(user_name,email,password):
    connection=mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor=connection.cursor(dictionary=True)
        query = "SELECT * FROM digital_library.users WHERE email=%s AND password=%s"
        cursor.execute(query,(email,password,))
        result = cursor.fetchall()
        if result:
            print("kullanici zaten kayitli")
            return False
        
        query="""INSERT INTO digital_library.users(user_name,email,password)
                 VALUES(%s,%s,%s)"""
        cursor.execute(query,(user_name, email, password,))
        connection.commit()
        print("oldu")
        return True
       
    except Exception as e:
        return f"ERROR: {e}"

    finally:
        cursor.close()
        connection.close()
#print(Register_users("buse","b@mail.com","123"))

# models/users.py dosyasının sonuna ekleyin:

def get_user_by_email(email):
    """Email ile kullanıcı getir"""
    connection = mysql.connector.connect(**CONFIG)
    if not connection:
        return None
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM digital_library.users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        return user
    except Exception as e:
        print(f"Kullanıcı getirilemedi: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def authenticate_user(email: str, password: str):
    """Kullanıcı doğrulama"""
    user = get_user_by_email(email)
    if not user:
        return False
    # Şifre kontrolü için auth modülünü import et
    try:
        from auth import verify_password
        if not verify_password(password, user["password"]):
            return False
    except ImportError:
        # Eğer auth modülü yüklenemezse, basit string karşılaştırması yap
        if password != user["password"]:
            return False
    return user