import psycopg2
from psycopg2 import OperationalError
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# connection = psycopg2.connect(
#     database='new_app',
#     user='postgres',
#     password='root',
#     host='127.0.0.1',
#     port='5432',
# )
#
# mycursor = connection.cursor()
# # print(connection.get_dsn_parameters(), "\n")
# # Выполнение SQL-запроса
# mycursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'posts';")
# # Получить результат
# for x in mycursor:
#   print(x)


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print('Connection to PosrgresQL DB successfull')
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


con = create_connection(
    "new_app", "postgres", "root", "127.0.0.1", "5432"
)
print(con, '---------------------------------')


# def create_database(connection, query):
#     print(connection)
#     con.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print('Database created')
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
#
# create_name_bd = "CREATE DATABASE new_app"
# create_database(con, create_name_bd)


def create_table(connection, query):
    con.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL, 
  age INTEGER,
  gender TEXT,
  nationality TEXT
)
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  user_id INTEGER REFERENCES users(id)
)
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id SERIAL PRIMARY KEY,
  text TEXT NOT NULL,
  user_id INTEGER REFERENCES users(id),
  post_id INTEGER REFERENCES posts(id)
)
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id SERIAL PRIMARY KEY, 
  user_id INTEGER,
  post_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users (id),
  FOREIGN KEY (post_id) REFERENCES posts (id)
)
"""

# create_table(con, create_users_table)
# create_table(con, create_posts_table)
create_table(con, create_comments_table)
# create_table(con, create_likes_table)
