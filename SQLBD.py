import mysql.connector
from mysql.connector import connect, Error


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="admin",
#   password="root",
#   database="new_app"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection("localhost", "admin", "root", "new_app")


#
#
# # def create_database(connection):
# #     cursor = connection.cursor()
# #     try:
# #         cursor.execute("CREATE DATABASE new_app")
# #         print("Database created successfully")
# #     except Error as e:
# #         print(f"The error '{e}' occurred")
# #
# #
# # create_database(connection)
#
#
# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# create_users_table = """
# CREATE TABLE IF NOT EXISTS users (
#   id INT AUTO_INCREMENT,
#   name TEXT NOT NULL,
#   age INT,
#   gender TEXT,
#   nationality TEXT,
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """
#
# create_posts_table = """
# CREATE TABLE IF NOT EXISTS posts (
#   id INT AUTO_INCREMENT,
#   title TEXT NOT NULL,
#   description TEXT NOT NULL,
#   user_id INTEGER NOT NULL,
#   FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
#   PRIMARY KEY (id)
# ) ENGINE = InnoDB
# """
#
# create_comments_table = """
# CREATE TABLE IF NOT EXISTS comments (
#   id INT AUTO_INCREMENT,
#   text TEXT NOT NULL,
#   user_id INTEGER NOT NULL,
#   post_id INTEGER NOT NULL,
#   FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
#   FOREIGN KEY fk_post_id (post_id) REFERENCES posts(id),
#   PRIMARY KEY (id)
# )ENGINE = InnoDB
# """
#
# create_likes_table = """
# CREATE TABLE IF NOT EXISTS likes (
#   id INT AUTO_INCREMENT,
#   user_id INTEGER NOT NULL,
#   post_id INTEGER NOT NULL,
#   FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
#   FOREIGN KEY fk_post_id (post_id) REFERENCES posts(id),
#   PRIMARY KEY (id)
# )ENGINE = InnoDB
# """
#
# create_sos_table = """
# CREATE TABLE IF NOT EXISTS sos (
#   id INT AUTO_INCREMENT,
#   user_id INTEGER NOT NULL,
#   post_id INTEGER NOT NULL,
#   INDEX fk_user_id (user_id),
#   INDEX fk_post_id (post_id),
#   FOREIGN KEY (user_id) REFERENCES users(id),
#   FOREIGN KEY (post_id) REFERENCES posts(id),
#   PRIMARY KEY (id)
# )ENGINE = InnoDB
# """
#
# execute_query(connection, create_sos_table)
# # execute_query(connection, create_comments_table)


# def execute_query_users(connection):
#     cursor = connection.cursor()
#     try:
#         sql = "INSERT INTO users (name, age, gender, nationality) VALUES ( %s, %s, %s, %s )"
#         val = [('James', 25, 'male', 'USA'),
#                ('Leila', 32, 'female', 'France'),
#                ('Brigitte', 35, 'female', 'England'),
#                ('Mike', 40, 'male', 'Denmark'),
#                ('Elizabeth', 21, 'female', 'Canada')
#                ]
#
#         cursor.executemany(sql, val)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# execute_query_users(connection)


# def execute_query_posts(connection):
#     cursor = connection.cursor()
#     try:
#         sql = "INSERT INTO posts (title, description, user_id) VALUES ( %s, %s, %s )"
#         val = [
#             ("Happy", "I am feeling very happy today", 1),
#             ("Hot Weather", "The weather is very hot today", 2),
#             ("Help", "I need some help with my work", 2),
#             ("Great News", "I am getting married", 1),
#             ("Interesting Game", "It was a fantastic game of tennis", 5),
#             ("Party", "Anyone up for a late-night party today?", 3)
#         ]
#
#         cursor.executemany(sql, val)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# execute_query_posts(connection)

# def execute_query_comments(connection):
#     cursor = connection.cursor()
#     try:
#         sql = "INSERT INTO comments (text, user_id, post_id) VALUES ( %s, %s, %s )"
#         val = [
#             ('Count me in', 1, 6),
#             ('What sort of help?', 5, 3),
#             ('Congrats buddy', 2, 4),
#             ('I was rooting for Nadal though', 4, 5),
#             ('Help with your thesis?', 2, 3),
#             ('Many congratulations', 5, 4)
#         ]
#
#         cursor.executemany(sql, val)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# execute_query_comments(connection)


# def execute_query_likes(connection):
#     cursor = connection.cursor()
#     try:
#         sql = "INSERT INTO likes (user_id, post_id) VALUES ( %s, %s )"
#         val = [
#             (1, 6),
#             (2, 3),
#             (1, 5),
#             (5, 4),
#             (2, 4),
#             (4, 2),
#             (3, 6)
#         ]
#
#         cursor.executemany(sql, val)
#         connection.commit()
#         print("Query executed successfully")
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# execute_query_likes(connection)

# def execute_query_read_table(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# reads_users = "SELECT * FROM users"
# users = execute_query_read_table(connection, reads_users)
#
# for user in users:
#     print(user)

def execute_query_read_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# reads_users = """
# SELECT
#   users.name,
#   posts.description,
#   COUNT(likes.id) as likes
# FROM
#   users,
#   posts,
#   likes
# WHERE
#   users.id = posts.user_id
# AND
#   posts.id = likes.post_id
# GROUP BY
#   likes.post_id
# """

reads_users = """
SELECT
  users.name,
  posts.description
FROM
  users
INNER JOIN posts ON users.id = posts.user_id
"""
users = execute_query_read_table(connection, reads_users)

for user in users:
    print(user)