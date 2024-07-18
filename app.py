#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename

from datetime import datetime

from dateutil import parser

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
import datosConfiguraciones as config
#--------------------------------------------------------------------

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

class Turnos:
    #----------------------------------------------------------------
    # Constructor de la clase
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
            
        # Function to check if a table exists
        def table_exists(table_name):
            self.cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            result = self.cursor.fetchone()
            return result is not None
        
        if not table_exists('Clientes'):
            self.cursor.execute('''CREATE TABLE Clientes (
                ClienteID INT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(50) NOT NULL,
                Apellido VARCHAR(50) NOT NULL,
                Telefono VARCHAR(15),
                Email VARCHAR(50) NOT NULL
            );''')
        
        
        if not table_exists('Barberos'):
            self.cursor.execute('''CREATE TABLE Barberos (
                BarberoID INT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(50) NOT NULL,
                Apellido VARCHAR(50) NOT NULL,
                Telefono VARCHAR(15),
                Email VARCHAR(50)                 
            );''')

        if not table_exists('Servicios'):
            self.cursor.execute('''CREATE TABLE Servicios (
                ServicioID INT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(50) NOT NULL,
                Duracion INT NOT NULL, -- Duración en minutos
                Precio DECIMAL(10, 2) NOT NULL
            );''')

        if not table_exists('Turnos'):
            self.cursor.execute('''CREATE TABLE Turnos (
                TurnoID INT AUTO_INCREMENT PRIMARY KEY,
                ClienteID INT NOT NULL,
                BarberoID INT NOT NULL,
                ServicioID INT NOT NULL,
                FechaHora DATETIME NOT NULL,
                Mensaje TEXT,
                Imagen_url VARCHAR(255),
                Estado ENUM('Programado', 'Completado', 'Cancelado') DEFAULT 'Programado',
                FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
                FOREIGN KEY (BarberoID) REFERENCES Barberos(BarberoID),
                FOREIGN KEY (ServicioID) REFERENCES Servicios(ServicioID)
            );''')
        self.conn.commit()
        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host=config.host,
                user=config.user,
                password=config.password,
                database=config.database
            )
            self.cursor = self.conn.cursor()
        except:
            print('Ocurrio un error abriendo la conexion')
    
    def desconectar(self):
        try:
            self.cursor.close()
            self.conn.close()
        except:
            print('Ocurrio un error cerrndo la conexion')


    def listar_turnos(self):
        self.conectar()
        self.cursor.execute("SELECT * FROM Turnos")
        turnos = self.cursor.fetchall()
        print(turnos)
        self.desconectar()
        return turnos
    
    def consultar_turno(self, TurnoID):
        # Consultamos un turno a partir de su código
        self.cursor.execute(f"SELECT * FROM Turnos WHERE TurnoID = {TurnoID}")

        return self.cursor.fetchone()
    
    def get_appointment_by_turno_id(self, turno_id):
        self.cursor.callproc('GetAppointmentByTurnoID', [turno_id])
        for result in self.cursor.stored_results():
            return result.fetchall()

    def consultar_turno_por_Fecha(self, turno_fecha):
        # Consultamos un turno a partir de su código
        self.cursor.execute(f"SELECT * FROM Turnos WHERE FechaHora = {turno_fecha}")
        return self.cursor.fetchone()

    def mostrar_turno(self, TurnoID):
        
        # Mostramos los datos de un turno a partir de su código
        turno = self.consultar_turno(TurnoID)
        if turno:
            print("-" * 40)
            print(f"TurnoID....: {turno['TurnoID']}")
            print(f"Nombre.....: {turno['Nombre']}")
            print(f"Apellido...: {turno['Apellido']}")
            print(f"Email......: {turno['Email']}")
            print(f"Imagen_url.: {turno['imagen_url']}")
            print(f"Telefono...: {turno['Telefono']}")
            print(f"FechaHora..: {turno['FechaHora']}")
            print(f"Mensaje....: {turno['Mensaje']}")
            print("-" * 40)
        else:
            print("Turno no encontrado.")

    def agregar_turno(self, Nombre, Apellido, Email, Imagen, Telefono, FechaHora, Mensaje):
        sql = "INSERT INTO Turnos ( Nombre, Apellido, Email, Imagen_url, Telefono, FechaHora, Mensaje) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (Nombre, Apellido, Email, Imagen, Telefono, FechaHora, Mensaje)
        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_turno(self, TurnoID, nuevo_Nombre, nuevo_Apellido, nuevo_Email, nueva_Imagen, nuevo_Telefono, nueva_FechaHora, nuevo_Mensaje):
        sql = "UPDATE Turnos SET Nombre = %s, Apellido = %s, Email = %s, Imagen_url = %s, Telefono = %s, FechaHora = %s, Mensaje = %s WHERE TurnoID = %s"
        valores = (nuevo_Nombre, nuevo_Apellido, nuevo_Email, nueva_Imagen, nuevo_Telefono ,nueva_FechaHora, nuevo_Mensaje, TurnoID)
        try:
            self.cursor.execute(sql, valores)
            self.conn.commit()
            print("Turno actualizado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        return self.cursor.rowcount > 0

    def eliminar_turno(self, TurnoID):
        # Eliminamos un turno de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM TURNOS WHERE TurnoID = {TurnoID}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def get_all_appointments(self):
        self.cursor.callproc('GetAllAppointments')
        for result in self.cursor.stored_results():
            return result.fetchall()

    def get_appointments_by_client(self, client_id):
        self.cursor.callproc('GetAppointmentsByClient', [client_id])
        for result in self.cursor.stored_results():
            for row in result.fetchall():
                print(row)

    def get_appointments_by_barber(self, barber_id):
        self.cursor.callproc('GetAppointmentsByBarber', [barber_id])
        for result in self.cursor.stored_results():
            for row in result.fetchall():
                print(row)

    def get_appointments_by_date_range(self, start_date, end_date):
        self.cursor.callproc('GetAppointmentsByDateRange', [start_date, end_date])
        for result in self.cursor.stored_results():
            for row in result.fetchall():
                print(row)


#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase CatalogoCatalogo
# Uso de archivo de configuraciones
turnosCatalogo = Turnos(host=config.host, 
                        user=config.user,
                        password=config.password, 
                        database=config.database)

# Carpeta para guardar las imagenes
ruta_destino = config.rutaDestino

@app.route("/turnos", methods=["GET"])
def listar_turnos():
    turnos = turnosCatalogo.get_all_appointments()
    # turnos = turnosCatalogo.listar_turnos()
    return jsonify(turnos)

@app.route("/turnos/<int:turnoId>", methods=["GET"])
def mostrar_turno(turnoId):
    turno = turnosCatalogo.get_appointment_by_turno_id(turnoId)
    if turno:
        return jsonify(turno)
    else:
        return "Turno no encontrado", 404

@app.route("/turnos/<string:turno_fecha>", methods=["GET"])
def mostrar_turno_por_fecha(turno_fecha):
    datetime_object = datetime.strptime(turno_fecha, '%Y/%m/%d %H:%M')
    print("-" * 30)
    print( datetime_object)
    turno = turnosCatalogo.consultar_turno_por_Fecha(datetime_object)
    if turno:
        return jsonify(turno)
    else:
        return "Turno no encontrado", 404


@app.route("/turnos", methods=["POST"])
def agregar_turno():
    #Recojo los datos del form
    
    Nombre= request.form['nombre']
    Apellido= request.form['apellido']
    email= request.form['email']
    imagen= request.files['imagen']
    telefono= request.form['telefono']
    mensaje= request.form['mensaje']
    fecha_Hora= request.form['datetimepicker'] 
    
    # Genero el nombre de la imagen
    nombre_imagen = secure_filename(imagen.filename) 
    nombre_base, extension = os.path.splitext(nombre_imagen) 
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" 

    nuevo_turnoID = turnosCatalogo.agregar_turno(Nombre,Apellido,email,nombre_imagen,telefono,fecha_Hora,mensaje)
    if nuevo_turnoID:    
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        return jsonify({"mensaje": "Turno agregado correctamente.", "nuevo_turnoID": nuevo_turnoID, "imagen": nombre_imagen}), 201
    else:
        return jsonify({"mensaje": "Error al agregar el turno."}), 500

@app.route("/turnos/<int:turnoID>", methods=["PUT"])
def modificar_turno(turnoID):
    #Se recuperan los nuevos datos del formulario
    nuevo_Nombre= request.form["nombre"]
    nuevo_Apellido= request.form["apellido"]
    nuevo_email= request.form["email"]
    nuevo_telefono= request.form["telefono"]
    nuevo_mensaje= request.form["mensaje"]
    nueva_fecha_Hora= request.form["fecha"]
    
    # Verifica si se proporcionó una nueva imagen
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        # Procesamiento de la imagen
        nombre_imagen = secure_filename(imagen.filename) 
        nombre_base, extension = os.path.splitext(nombre_imagen) 
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" 

        # Guardar la imagen en el servidor
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        
        # Busco el turno guardado
        turno = turnosCatalogo.consultar_turno(turnoID)
        if turno: # Si existe el turno...
            imagen_vieja = turno["Imagen_url"]
            # Armo la ruta a la imagen
            ruta_imagen = os.path.join(ruta_destino, imagen_vieja)

            # Y si existe la borro.
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
    else:     
        turno = turnosCatalogo.consultar_turno(turnoID)
        if turno:
            nombre_imagen = turno["Imagen_url"]

   # Se llama al método modificar_turno pasando el turnoID del turno y los nuevos datos.
    if turnosCatalogo.modificar_turno(turnoID,nuevo_Nombre, nuevo_Apellido, nuevo_email, nombre_imagen, nuevo_telefono, nueva_fecha_Hora, nuevo_mensaje):
        return jsonify({"mensaje": "Turno modificado"}), 200
    else:
        return jsonify({"mensaje": "Turno no encontrado"}), 403

@app.route("/turnos/<int:turnoID>", methods=["DELETE"])
def eliminar_turno(turnoID):
    # Primero, obtiene la información del turno para encontrar la imagen
    turno = turnosCatalogo.consultar_turno(turnoID)
    if turno:
        # Eliminar la imagen asociada si existe
        ruta_imagen = os.path.join(ruta_destino, turno['Imagen_url'])
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

        # Luego, elimina el turno del catálogo
        if turnosCatalogo.eliminar_turno(turnoID):
            return jsonify({"mensaje": "Turno eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el Turno"}), 500
    else:
        return jsonify({"mensaje": "Turno no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)