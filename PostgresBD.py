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


# def create_table(connection, query):
#     con.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
#
# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#   id SERIAL PRIMARY KEY,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   nationality TEXT
# )
# """
#
# create_posts_table = """
# CREATE TABLE IF NOT EXISTS posts (
#   id SERIAL PRIMARY KEY,
#   title TEXT NOT NULL,
#   description TEXT NOT NULL,
#   user_id INTEGER REFERENCES users(id)
# )
# """
#
# create_comments_table = """
# CREATE TABLE IF NOT EXISTS comments (
#   id SERIAL PRIMARY KEY,
#   text TEXT NOT NULL,
#   user_id INTEGER REFERENCES users(id),
#   post_id INTEGER REFERENCES posts(id)
# )
# """
#
# create_likes_table = """
# CREATE TABLE IF NOT EXISTS likes (
#   id SERIAL PRIMARY KEY,
#   user_id INTEGER,
#   post_id INTEGER,
#   FOREIGN KEY (user_id) REFERENCES users (id),
#   FOREIGN KEY (post_id) REFERENCES posts (id)
# )
# """

# create_table(con, create_users_table)
# create_table(con, create_posts_table)
# create_table(con, create_comments_table)
# create_table(con, create_likes_table)

# def execute_query_users(connection):
#     try:
#         users = [
#             ("James", 25, "male", "USA"),
#             ("Leila", 32, "female", "France"),
#             ("Brigitte", 35, "female", "England"),
#             ("Mike", 40, "male", "Denmark"),
#             ("Elizabeth", 21, "female", "Canada"),
#         ]
#
#         user_records = ", ".join(["%s"] * len(users))
#
#         insert_query = (
#             f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"
#         )
#
#         connection.autocommit = True
#         cursor = connection.cursor()
#         cursor.execute(insert_query, users)
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
#
# execute_query_users(con)


# def create_table(connection):
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute("DELETE FROM users WHERE id > 6")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
# create_table(con)

# def execute_query_posts(connection):
#     try:
#         posts = [
#             ("Happy", "I am feeling very happy today", 1),
#             ("Hot Weather", "The weather is very hot today", 2),
#             ("Help", "I need some help with my work", 2),
#             ("Great News", "I am getting married", 1),
#             ("Interesting Game", "It was a fantastic game of tennis", 5),
#             ("Party", "Anyone up for a late-night party today?", 3)
#         ]
#
#         posts_records = ", ".join(["%s"] * len(posts))
#
#         insert_query = (
#             f"INSERT INTO posts (title, description, user_id) VALUES {posts_records}"
#         )
#
#         connection.autocommit = True
#         cursor = connection.cursor()
#         cursor.execute(insert_query, posts)
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
#
# execute_query_posts(con)

# def execute_query_comments(connection):
#     try:
#         comments = [
#             ('Count me in', 1, 6),
#             ('What sort of help?', 5, 3),
#             ('Congrats buddy', 2, 4),
#             ('I was rooting for Nadal though', 4, 5),
#             ('Help with your thesis?', 2, 3),
#             ('Many congratulations', 5, 4)
#         ]
#
#         posts_records = ", ".join(["%s"] * len(comments))
#
#         insert_query = (
#             f"INSERT INTO comments (text, user_id, post_id) VALUES {posts_records}"
#         )
#
#         connection.autocommit = True
#         cursor = connection.cursor()
#         cursor.execute(insert_query, comments)
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
#
# execute_query_comments(con)

# def execute_query_likes(connection):
#     try:
#         likes = [
#             (1, 6),
#             (2, 3),
#             (1, 5),
#             (5, 4),
#             (2, 4),
#             (4, 2),
#             (3, 6)
#         ]
#
#         posts_records = ", ".join(["%s"] * len(likes))
#
#         insert_query = (
#             f"INSERT INTO likes (user_id, post_id) VALUES {posts_records}"
#         )
#
#         connection.autocommit = True
#         cursor = connection.cursor()
#         cursor.execute(insert_query, likes)
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
#
# execute_query_likes(con)

def execute_query_read_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


reads_users = "SELECT * FROM users"
users = execute_query_read_table(con, reads_users)

for user in users:
    print(user)