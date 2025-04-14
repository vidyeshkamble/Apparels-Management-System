import mysql



class FetchDataFromDatabase:
    def __init__(self,id):
        self.id= id
        

    @staticmethod
    def Connection():
        return mysql.connector.connect(
            host="localhost", # Host name
            user="root", # User Id of your Database
            password="system", # Password of your Database
            database="apparels" # Keep your database name as 'apparels'
        )
    
    def Customer(self):
        mydb = self.Connection()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM apparels.customer where user_id = %s",(self.id,))
        myresultarray = mycursor.fetchone()
        mydb.close()
        mycursor.close()
        return myresultarray
    