from psycopg2 import connect
from psycopg2.errors import UniqueViolation
from config import DB_NAME, DB_PASS, DB_PORT, DB_USER, DB_ADDRESS
import time


def db_connect():
    """Connect with db"""
    database = connect(dbname=DB_NAME,
                       host=DB_ADDRESS,
                       port=DB_PORT,
                       user=DB_USER,
                       password=DB_PASS)

    return database


def create_table():
    """Create table"""
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS aloqabank_history(
            history_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            date BIGINT,        
            currency_purchase VARCHAR(50),
            currency_sale VARCHAR(50),
            currency_cbu VARCHAR(50)
        );

    CREATE TABLE IF NOT EXISTS aloqabank_users(
            user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            telegram_id BIGINT UNIQUE   
        );

    ''')
    database.commit()
    database.close()


def insert_or_ignore_user(chat_id: int) -> bool:
    database = db_connect()
    cursor = database.cursor()
    try:
        cursor.execute('''
        INSERT INTO aloqabank_users(telegram_id) VALUES (%s)
        ''', (chat_id,))
        database.commit()
        return True
    except UniqueViolation:
        return False
    finally:
        database.close()


def insert_currency(purchase: str, sale: str, cbu: str) -> None:
    """Запись историии в БД"""
    unix_time = int(time.time())
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO aloqabank_history(date, currency_purchase, currency_sale, currency_cbu)
    VALUES (%s, %s, %s, %s)
    ''', (unix_time, purchase, sale, cbu))

    database.commit()
    database.close()


def get_last_currency() -> tuple:
    """Получаем последнюю запись"""
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    SELECT currency_purchase, currency_sale, currency_cbu 
    FROM aloqabank_history 
    ORDER BY history_id DESC LIMIT 1;
    ''')
    result = cursor.fetchone()
    database.close()
    return result


def get_all_subscribers() -> list:
    """Получаем список подписчиков"""
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    SELECT telegram_id FROM aloqabank_users;
    ''')
    result = cursor.fetchall()
    database.close()
    return result


def delete_user(chat_id: int) -> None:
    """Удаляем пользователя, если он отписался"""
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM aloqabank_users WHERE telegram_id = %s;
    ''', (chat_id,))

    database.commit()
    database.close()


if __name__ == '__main__':
    create_table()