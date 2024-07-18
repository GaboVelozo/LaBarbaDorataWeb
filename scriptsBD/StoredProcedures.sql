DELIMITER //

CREATE PROCEDURE GetAllAppointments()
BEGIN
    SELECT
        t.TurnoID,
        t.Imagen_url,
        t.Mensaje,
        t.FechaHora,
        t.Estado,
        c.ClienteID,
        c.Nombre AS ClienteNombre,
        c.Apellido AS ClienteApellido,
        c.Telefono AS ClienteTelefono,
        c.Email AS ClienteEmail,
        b.BarberoID,
        b.Nombre AS BarberoNombre,
        b.Apellido AS BarberoApellido,
        b.Telefono AS BarberoTelefono,
        b.Email AS BarberoEmail,
        s.ServicioID,
        s.Nombre AS ServicioNombre,
        s.Duracion AS ServicioDuracion,
        s.Precio AS ServicioPrecio
    FROM
        Turnos t
    INNER JOIN Clientes c ON t.ClienteID = c.ClienteID
    INNER JOIN Barberos b ON t.BarberoID = b.BarberoID
    INNER JOIN Servicios s ON t.ServicioID = s.ServicioID;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetAppointmentByTurnoID(IN turno_id INT)
BEGIN
    SELECT
        t.TurnoID,
        t.Imagen_url,
        t.Mensaje,
        t.FechaHora,
        t.Estado,
        c.ClienteID,
        c.Nombre AS ClienteNombre,
        c.Apellido AS ClienteApellido,
        c.Telefono AS ClienteTelefono,
        c.Email AS ClienteEmail,
        b.BarberoID,
        b.Nombre AS BarberoNombre,
        b.Apellido AS BarberoApellido,
        b.Telefono AS BarberoTelefono,
        b.Email AS BarberoEmail,
        s.ServicioID,
        s.Nombre AS ServicioNombre,
        s.Duracion AS ServicioDuracion,
        s.Precio AS ServicioPrecio
    FROM
        Turnos t
    INNER JOIN Clientes c ON t.ClienteID = c.ClienteID
    INNER JOIN Barberos b ON t.BarberoID = b.BarberoID
    INNER JOIN Servicios s ON t.ServicioID = s.ServicioID
    WHERE t.TurnoID = turno_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetAppointmentsByClient(IN client_id INT)
BEGIN
    SELECT
        t.TurnoID,
        t.Imagen_url,
        t.Mensaje,
        t.FechaHora,
        t.Estado,
        c.ClienteID,
        c.Nombre AS ClienteNombre,
        c.Apellido AS ClienteApellido,
        c.Telefono AS ClienteTelefono,
        c.Email AS ClienteEmail,
        b.BarberoID,
        b.Nombre AS BarberoNombre,
        b.Apellido AS BarberoApellido,
        b.Telefono AS BarberoTelefono,
        b.Email AS BarberoEmail,
        s.ServicioID,
        s.Nombre AS ServicioNombre,
        s.Duracion AS ServicioDuracion,
        s.Precio AS ServicioPrecio
    FROM
        Turnos t
    INNER JOIN Clientes c ON t.ClienteID = c.ClienteID
    INNER JOIN Barberos b ON t.BarberoID = b.BarberoID
    INNER JOIN Servicios s ON t.ServicioID = s.ServicioID
    WHERE t.ClienteID = client_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetAppointmentsByBarber(IN barber_id INT)
BEGIN
    SELECT
        t.TurnoID,
        t.Imagen_url,
        t.Mensaje,
        t.FechaHora,
        t.Estado,
        c.ClienteID,
        c.Nombre AS ClienteNombre,
        c.Apellido AS ClienteApellido,
        c.Telefono AS ClienteTelefono,
        c.Email AS ClienteEmail,
        b.BarberoID,
        b.Nombre AS BarberoNombre,
        b.Apellido AS BarberoApellido,
        b.Telefono AS BarberoTelefono,
        b.Email AS BarberoEmail,
        s.ServicioID,
        s.Nombre AS ServicioNombre,
        s.Duracion AS ServicioDuracion,
        s.Precio AS ServicioPrecio
    FROM
        Turnos t
    INNER JOIN Clientes c ON t.ClienteID = c.ClienteID
    INNER JOIN Barberos b ON t.BarberoID = b.BarberoID
    INNER JOIN Servicios s ON t.ServicioID = s.ServicioID
    WHERE t.BarberoID = barber_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetAppointmentsByDateRange(IN start_date DATETIME, IN end_date DATETIME)
BEGIN
    SELECT
        t.TurnoID,
        t.Imagen_url,
        t.Mensaje,
        t.FechaHora,
        t.Estado,
        c.ClienteID,
        c.Nombre AS ClienteNombre,
        c.Apellido AS ClienteApellido,
        c.Telefono AS ClienteTelefono,
        c.Email AS ClienteEmail,
        b.BarberoID,
        b.Nombre AS BarberoNombre,
        b.Apellido AS BarberoApellido,
        b.Telefono AS BarberoTelefono,
        b.Email AS BarberoEmail,
        s.ServicioID,
        s.Nombre AS ServicioNombre,
        s.Duracion AS ServicioDuracion,
        s.Precio AS ServicioPrecio
    FROM
        Turnos t
    INNER JOIN Clientes c ON t.ClienteID = c.ClienteID
    INNER JOIN Barberos b ON t.BarberoID = b.BarberoID
    INNER JOIN Servicios s ON t.ServicioID = s.ServicioID
    WHERE t.FechaHora BETWEEN start_date AND end_date;
END //

DELIMITER ;
