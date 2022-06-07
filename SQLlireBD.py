import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to SQLite BD successfull')
    except Error as e:
        print(f'The error {e} occurred')
    return connection


connect = create_connection("sqlsm.sqlite3")


# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#     except Error as e:
#         print(f'The error {e} occurred')
#     return connection
#
#
# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT NOT NULL,
#   age INTEGER,
#   gender TEXT,
#   nationality TEXT
# );
# """
#
# create_posts_table = """
# CREATE TABLE IF NOT EXISTS posts(
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   title TEXT NOT NULL,
#   description TEXT NOT NULL,
#   user_id INTEGER NOT NULL,
#   FOREIGN KEY (user_id) REFERENCES users (id)
# );
# """
#
# create_comments_table = """
# CREATE TABLE IF NOT EXISTS comments (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# text TEXT NOT NULL,
# user_id INTEGER NOT NULL,
# post_id INTEGER NOT NULL,
# FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES post (id)
# );
# """
#
# create_likes_table = """
# CREATE TABLE IF NOT EXISTS likes (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   user_id INTEGER NOT NULL,
#   post_id INTEGER NOT NULL,
#   FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
# );
# """
#
# execute_query(connect, create_likes_table)

# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#     except Error as e:
#         print(f'The error {e} occurred')
#     return connection
#
#
# create_users = """
# INSERT INTO
#   users (name, age, gender, nationality)
# VALUES
#   ('James', 25, 'male', 'USA'),
#   ('Leila', 32, 'female', 'France'),
#   ('Brigitte', 35, 'female', 'England'),
#   ('Mike', 40, 'male', 'Denmark'),
#   ('Elizabeth', 21, 'female', 'Canada');
# """
# create_posts = """
# INSERT INTO
#   posts (title, description, user_id)
# VALUES
#   ("Happy", "I am feeling very happy today", 1),
#   ("Hot Weather", "The weather is very hot today", 2),
#   ("Help", "I need some help with my work", 2),
#   ("Great News", "I am getting married", 1),
#   ("Interesting Game", "It was a fantastic game of tennis", 5),
#   ("Party", "Anyone up for a late-night party today?", 3);
# """
#
# create_comments = """
# INSERT INTO
#   comments (text, user_id, post_id)
# VALUES
#   ('Count me in', 1, 6),
#   ('What sort of help?', 5, 3),
#   ('Congrats buddy', 2, 4),
#   ('I was rooting for Nadal though', 4, 5),
#   ('Help with your thesis?', 2, 3),
#   ('Many congratulations', 5, 4);
# """
#
# create_likes = """
# INSERT INTO
#   likes (user_id, post_id)
# VALUES
#   (1, 6),
#   (2, 3),
#   (1, 5),
#   (5, 4),
#   (2, 4),
#   (4, 2),
#   (3, 6);
# """
#
# execute_query(connect, create_posts)
# execute_query(connect, create_users)
# execute_query(connect, create_comments)
# execute_query(connect, create_likes)

def execute_select(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'The error {e} occurred')
execute_tables_users = "SELECT * FROM users"
result_user = execute_select(connect, execute_tables_users)

for user in result_user:
    print(user, '===========')


