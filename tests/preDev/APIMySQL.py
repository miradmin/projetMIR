import mysql.connector

queryCreateTableTests = ["CREATE TABLE `table1` (`property1` int(11))"]

config = {
    'user': 'testUser',
    'password': 'testPassword',
    'host': '127.0.0.1',
    'database': 'test'
}

class APIMySQL:
    def __init__(self):
        self.conexion = None
        self.cnx = None

    def createDB(self):
        try:
            self.cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(config['database']));
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**config)
            self.cursor = self.conexion.cursor
        except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            self.createDB()
        else:
            print(err)
            

    def execute(self, query):
        self.cursor.execute(query)
        

def main():
    api = APIMySQL()
    api.connect()
    api.execute(queryCreateTableTests[0]);

