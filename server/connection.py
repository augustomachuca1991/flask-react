import mysql.connector

db_connection = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'flask-react-test'
}

def connect_db():
    try:
        connection = mysql.connector.connect(**db_connection)
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        raise

if __name__ == "__main__":
    connect_db()



