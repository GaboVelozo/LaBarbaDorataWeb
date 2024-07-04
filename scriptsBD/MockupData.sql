--INSERSION DE DATOS PARA TEST

INSERT INTO Clientes (Nombre, Apellido, Telefono, Email) VALUES
('Juan', 'Pérez', '555-1234', 'juan.perez@example.com'),
('María', 'González', '555-5678', 'maria.gonzalez@example.com'),
('Carlos', 'Rodríguez', '555-8765', 'carlos.rodriguez@example.com'),
('Ana', 'Martínez', '555-4321', 'ana.martinez@example.com');

INSERT INTO Barberos (Nombre, Apellido, Telefono) VALUES
('Pedro', 'López', '555-1111'),
('José', 'Hernández', '555-2222'),
('Luis', 'García', '555-3333'),
('Miguel', 'Ramírez', '555-4444');

INSERT INTO Servicios (Nombre, Duracion, Precio) VALUES
('Corte de Pelo', 30, 15.00),
('Afeitado', 20, 10.00),
('Corte y Barba', 45, 25.00),
('Tinte', 60, 40.00);

INSERT INTO Turnos (ClienteID, BarberoID, ServicioID, FechaHora, Estado) VALUES
(1, 1, 1, '2024-07-01 10:00:00', 'Programado'),
(2, 2, 2, '2024-07-01 11:00:00', 'Programado'),
(3, 3, 3, '2024-07-01 12:00:00', 'Programado'),
(4, 4, 4, '2024-07-01 13:00:00', 'Programado');
