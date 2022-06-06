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
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  name TEXT NOT NULL,
  age INT,
  gender TEXT,
  nationality TEXT,
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INT AUTO_INCREMENT,
  text TEXT NOT NULL,
  user_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
  FOREIGN KEY fk_post_id (post_id) REFERENCES posts(id),
  PRIMARY KEY (id)
)ENGINE = InnoDB
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INT AUTO_INCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY fk_user_id (user_id) REFERENCES users(id),
  FOREIGN KEY fk_post_id (post_id) REFERENCES posts(id),
  PRIMARY KEY (id)
)ENGINE = InnoDB
"""

create_sos_table = """
CREATE TABLE IF NOT EXISTS sos (
  id INT AUTO_INCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  INDEX fk_user_id (user_id),
  INDEX fk_post_id (post_id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (post_id) REFERENCES posts(id),
  PRIMARY KEY (id)
)ENGINE = InnoDB
"""

execute_query(connection, create_sos_table)
# execute_query(connection, create_comments_table)
