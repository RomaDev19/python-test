import sqlite3


try:
    # connection to db or create new
    connection = sqlite3.connect("acountant.db")
    # create object cursor
    cursor = connection.cursor()

    #create user with users_id = 1000 Теперь вы можете использовать объект cursor для выполнения SQL-запросов
    cursor.execute("INSERT OR IGNORE INTO `users` (`user_id`) VALUES (?)", (1000,))

    #Считываем всех пользователей
    users = cursor.execute("SELECT * FROM `users`")
    print(users.fetchall())

    # Фиксация изменений в базе данных
    connection.commit()

except sqlite3.Error as error:
    print("Error", error)

finally:
    if(connection):
        connection.close()