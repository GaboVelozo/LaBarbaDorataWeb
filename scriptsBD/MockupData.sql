-- Insert data into Clientes table
INSERT INTO Clientes (Nombre, Apellido, Telefono, Email) VALUES
('Juan', 'Perez', '1234567890', 'juan.perez@example.com'),
('Maria', 'Gonzalez', '0987654321', 'maria.gonzalez@example.com'),
('Carlos', 'Rodriguez', '1112223333', 'carlos.rodriguez@example.com'),
('Ana', 'Martinez', '4445556666', 'ana.martinez@example.com'),
('Luis', 'Hernandez', '7778889999', 'luis.hernandez@example.com');

-- Insert data into Barberos table
INSERT INTO Barberos (Nombre, Apellido, Telefono, Email) VALUES
('Pedro', 'Lopez', '1231231234', 'pedro.lopez@barbershop.com'),
('Miguel', 'Diaz', '4564564567', 'miguel.diaz@barbershop.com'),
('Jose', 'Sanchez', '7897897890', 'jose.sanchez@barbershop.com'),
('Fernando', 'Garcia', '1010101010', 'fernando.garcia@barbershop.com'),
('Ricardo', 'Ramos', '2020202020', 'ricardo.ramos@barbershop.com');

-- Insert data into Servicios table
INSERT INTO Servicios (Nombre, Duracion, Precio) VALUES
('Corte de pelo', 30, 15.00),
('Afeitado', 20, 10.00),
('Corte y barba', 45, 25.00),
('Tinte de pelo', 60, 30.00),
('Limpieza facial', 50, 20.00);

-- Insert data into Turnos table
INSERT INTO Turnos (Imagen_url, Mensaje, ClienteID, BarberoID, ServicioID, FechaHora, Estado) VALUES
('https://example.com/image1.jpg', 'Corte de pelo clásico', 1, 1, 1, '2024-07-20 10:00:00', 'Programado'),
('https://example.com/image2.jpg', 'Afeitado completo', 2, 2, 2, '2024-07-20 11:00:00', 'Programado'),
('https://example.com/image3.jpg', 'Corte y barba', 3, 3, 3, '2024-07-20 12:00:00', 'Programado'),
('https://example.com/image4.jpg', 'Tinte de pelo moderno', 4, 4, 4, '2024-07-20 13:00:00', 'Programado'),
('https://example.com/image5.jpg', 'Limpieza facial profunda', 5, 5, 5, '2024-07-20 14:00:00', 'Programado'),
('https://example.com/image6.jpg', 'Corte de pelo', 1, 2, 1, '2024-07-21 10:00:00', 'Completado'),
('https://example.com/image7.jpg', 'Afeitado', 2, 3, 2, '2024-07-21 11:00:00', 'Completado'),
('https://example.com/image8.jpg', 'Corte y barba', 3, 4, 3, '2024-07-21 12:00:00', 'Cancelado'),
('https://example.com/image9.jpg', 'Tinte de pelo', 4, 5, 4, '2024-07-21 13:00:00', 'Completado'),
('https://example.com/image10.jpg', 'Limpieza facial', 5, 1, 5, '2024-07-21 14:00:00', 'Cancelado');
