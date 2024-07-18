--creacion de tablas:
-- Tabla: Clientes
CREATE TABLE Clientes (
    ClienteID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(15),
    Email VARCHAR(50)
);

-- Tabla: Barberos
CREATE TABLE Barberos (
    BarberoID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(15),
    Email VARCHAR(50) NOT NULL
);

-- Tabla: Servicios
CREATE TABLE Servicios (
    ServicioID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Duracion INT NOT NULL, -- Duración en minutos
    Precio DECIMAL(10, 2) NOT NULL
);

-- Tabla: Turnos
CREATE TABLE Turnos (
    TurnoID INT AUTO_INCREMENT PRIMARY KEY,
    Imagen_url VARCHAR(255),
    Mensaje TEXT,
    ClienteID INT NOT NULL,
    BarberoID INT NOT NULL,
    ServicioID INT NOT NULL,
    FechaHora DATETIME NOT NULL,
    Estado ENUM('Programado', 'Completado', 'Cancelado') DEFAULT 'Programado',
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
    FOREIGN KEY (BarberoID) REFERENCES Barberos(BarberoID),
    FOREIGN KEY (ServicioID) REFERENCES Servicios(ServicioID)
);


