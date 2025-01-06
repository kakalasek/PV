import mysql.connector

class UserFacade():
    
    def __init__(self):
        self.connection = mysql.connector.connect(
                            host="127.0.0.1",
                            user="app1user",
                            password="student",
                            database="app1"
                            )
        self.userCursor = self.connection.cursor()
        
    def __del__(self):
        self.connection.close()

    def createUser(self, username, favorite_number, favorite_color):
        sqlCreateUser = "INSERT INTO User(username, favorite_number, favorite_color) VALUES(%s, %s, %s);"
        values = (username, favorite_number, favorite_color)

        self.userCursor.execute(sqlCreateUser, values)

        self.connection.commit()

    def readUserByUsername(self, username):
        sqlReadUserByUsername = "SELECT * FROM User WHERE username = %s;"
        values = (username,)

        self.userCursor.execute(sqlReadUserByUsername, values)

        selectedRecords = self.userCursor.fetchall()


        return selectedRecords.pop()
    
    def readUsers(self):

        sqlReadUserByUsername = "SELECT * FROM User;"

        self.userCursor.execute(sqlReadUserByUsername)

        selectedRecords = self.userCursor.fetchall()

        return selectedRecords
    
    def updateUsersFavoriteNumber(self, new_favorite_number, id):
        sqlUpdateUsersFavoriteNumber = "UPDATE User SET favorite_number = %s WHERE id = %s;"
        values = (new_favorite_number, id)

        self.userCursor.execute(sqlUpdateUsersFavoriteNumber, values)

        self.connection.commit()
    
    def updateUsersFavoriteColor(self, new_favorite_color, id):
        sqlUpdateUsersFavoriteColor = "UPDATE User SET favorite_color = %s WHERE id = %s;"
        values = (new_favorite_color, id)

        self.userCursor.execute(sqlUpdateUsersFavoriteColor, values)

        self.connection.commit()

    def deleteUser(self, id):
        sqlDeleteUser = "DELETE FROM User WHERE id = %s"
        values = (id,)

        self.userCursor.execute(sqlDeleteUser, values)

        self.connection.commit()
