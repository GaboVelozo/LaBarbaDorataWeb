
// LOCAL SETTINGS
// const URL = "http://127.0.0.1:5000/"
// PYTHONANYWHERE SETTINGS
const URL = "https://gabonline.pythonanywhere.com/"
// Variables de estado para controlar la visibilidad y los datos del formulario
let turnoId = '';
let nombre = '';
let apellido = '';
let email = '';
let telefono = '';
let mensaje = '';
let fecha = '';

let imagen_url = '';
let imagenSeleccionada = null;
let imagenUrlTemp = null;
let mostrarDatosTurno = false;

function validateForm() {
  let cumple = true;
  let nom = document.forms["contacto-form"]["nombre"].value;
  if (nom == "" || nom.length < 3) {
    document.getElementById('NombreError').hidden = false;
    cumple = false;
  } else document.getElementById('NombreError').hidden = true;

  let ape = document.forms["contacto-form"]["apellido"].value;
  if (ape == "" || ape.length < 3) {
    document.getElementById('ApellidoError').innerHTML = "Por favor ingrese su apellido";

    cumple = false;
  } else document.getElementById('ApellidoError').hidden = true;

  let email = document.forms["contacto-form"]["email"].value;
  const regexEmail =
    /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
  if (email == "" || !String(email).toLowerCase().match(regexEmail)) {
    document.getElementById('EmailError').innerHTML = "Por favor ingrese un direccion de correo electrónico válido";

    cumple = false;
  } else document.getElementById('EmailError').hidden = true;

  let tel = document.forms["contacto-form"]["telefono"].value;
  if (tel == "" || tel.length < 5) {
    document.getElementById('TelError').innerHTML = "Por favor ingrese un teléfono válido";

    cumple = false;
  } else document.getElementById('TelError').hidden = true;

  let msg = document.forms["contacto-form"]["mensaje"].value;
  if (msg == "" || msg.length < 3) {
    document.getElementById('MensajeError').innerHTML = "Por favor ingrese un mensaje";

    cumple = false;
  } else document.getElementById('MensajeError').hidden = true;

  if (cumple) {
    alert('Le responderemos a la brevedad! Gracias por su contacto!');
    return false;
  }
  else return cumple;
}


/// FUNCIONALIDADES TURNOS

//TRAER TURNOS
function obtenerListaTurnos() {
  // Realizamos la solicitud GET al servidor para obtener todos los turnos.
  fetch(URL + 'turnos')
    .then(function (response) {
      if (response.ok) {
        //Si la respuesta es exitosa (response.ok), convierte el cuerpo de la respuesta de formato JSON a un objeto JavaScript y pasa estos datos a la siguiente promesa then.
        return response.json();
      } else {
        // Si hubo un error, lanzar explícitamente una excepción para ser "catcheada" más adelante
        throw new Error('Error al obtener los turnos.');
      }
    })

    //Esta función maneja los datos convertidos del JSON.
    .then(function (data) {
      let tablaTurnos = document.getElementById('turnos-table'); //Selecciona el elemento del DOM donde se mostrarán los turnos.

      // Iteramos sobre cada turnos y agregamos filas a la tabla
      for (let turno of data) {
        let fila = document.createElement('tr'); //Crea una nueva fila de tabla (<tr>) para cada turno.
        fila.innerHTML = `
                    <th scope="row" style="color:white;">${turno.TurnoID}</th>
                    <td>${turno.Nombre}</td>
                    <td>${turno.Apellido}</td>
                    <td>${turno.Telefono}</td>
                    <td>${turno.Email}</td>
                    <td>${turno.FechaHora}</td>
                    <td align="center">${turno.Mensaje}</td>
                    <td><img src='${URL}static/imagenes/${turno.Imagen_url}' 
                        title="Click para agrandar" 
                        style="max-width: 100%; height: auto; " 
                        class="img-fluid img-thumbnail"
                        onclick="abrirImagen(this)">
                    <td>
                      <button class="btn btn-primary btn-sm fa-solid fa-user-xmark" onclick="eliminarTurno('${turno.TurnoID}')" title="Eliminar turno"></button>
                      
                      <button class="btn btn-primary btn-sm fa-solid fa-pen" onclick="window.location.href='modificarTurno.html?idTurno=${turno.TurnoID}'" title="Modificar turno"></button>
                    </td>
                    
                `;

        tablaTurnos.appendChild(fila);
      }
    })

    //Captura y maneja errores, mostrando una alerta en caso de error al obtener los turnos.
    .catch(function (error) {
      // Código para manejar errores
      alert('Error al obtener los turnos.');
    });
}



//ELIMINAR TURNOS
// Se utiliza para eliminar un turno.
function eliminarTurno(turnoId) {
  // Se muestra un diálogo de confirmación. Si el usuario confirma, se realiza una solicitud DELETE al servidor a través de fetch(URL + 'turnos/${turniD}', {method: 'DELETE' }).
  if (confirm('¿Estás seguro de que quieres eliminar este turno?')) {
    fetch(URL + `turnos/${turnoId}`, { method: 'DELETE' })
      .then(response => {
        if (response.ok) {
          // Si es exitosa (response.ok), elimina el turno y da mensaje de ok.
          //obtenerListaTurnos(); // Vuelve a obtener la lista de turnos para actualizar la tabla.
          location.reload();
          alert('Turno eliminado correctamente.');
        }
      })
      // En caso de error, mostramos una alerta con un mensaje de error.
      .catch(error => {
        alert(error.message);
      });
  }
}


//MODIFICAION DE TURNOS
// Se ejecuta cuando se envía el formulario de consulta. Realiza una solicitud GET a la API y obtiene los datos del turno correspondiente al código ingresado.
function obtenerTurno(event) {
  event.preventDefault();
  turnoId = document.getElementById('turnoID').value;
  fetch(URL + 'turnos/' + turnoId)
    .then(response => {
      if (response.ok) {
        return response.json()
      } else {
        throw new Error('Error al obtener los datos del turno.')
      }
    })
    .then(data => {
      nombre = data.Nombre;
      apellido = data.Apellido;
      telefono = data.Telefono;
      email = data.Email;
      mensaje = data.Mensaje;
      fecha = data.FechaHora;

      imagen_url = data.Imagen_url;
      mostrarDatosTurno = true; //Activa la vista del segundo formulario
      mostrarFormulario();
    })
    .catch(error => {
      alert('Id de turno no encontrado.');
    });
}

// Muestra el formulario con los datos del turno
function mostrarFormulario() {
  if (mostrarDatosTurno) {
    document.getElementById('nombreModificar').value = nombre;
    document.getElementById('apellidoModificar').value = apellido;
    document.getElementById('emailModificar').value = email;
    document.getElementById('telefonoModificar').value = telefono;

    const date = new Date(fecha);

    $('#datetimepickerModificar').datetimepicker('setOptions', { value: new Date(fecha) })

    document.getElementById('mensajeModificar').value = mensaje;

    const imagenActual = document.getElementById('imagen-actual');
    if (imagen_url && !imagenSeleccionada) { // Verifica si imagen_url no está vacía y no se ha seleccionado una imagen

      imagenActual.src = URL + 'static/imagenes/' + imagen_url;

      imagenActual.style.display = 'block'; // Muestra la imagen actual
    } else {
      imagenActual.style.display = 'none'; // Oculta la imagen si no hay URL
    }

    document.getElementById('datos-turno').style.display = 'block';
  } else {
    document.getElementById('datos-turno').style.display = 'none';
  }
}

// Se activa cuando el usuario selecciona una imagen para cargar.
function seleccionarImagen(event) {
  const file = event.target.files[0];
  imagenSeleccionada = file;
  imagenUrlTemp = URL.createObjectURL(file); // Crea una URL temporal para la vista previa

  const imagenVistaPrevia = document.getElementById('imagen-vista-previa');
  imagenVistaPrevia.src = imagenUrlTemp;
  imagenVistaPrevia.style.display = 'block';
}

// Se usa para enviar los datos modificados del turno al servidor.
function guardarCambios(event) {
  event.preventDefault();

  const formData = new FormData();
  formData.append('turnoId', turnoId);
  formData.append('nombre', document.getElementById('nombreModificar').value);
  formData.append('apellido', document.getElementById('apellidoModificar').value);
  formData.append('email', document.getElementById('emailModificar').value);
  formData.append('telefono', document.getElementById('telefonoModificar').value);
  formData.append('mensaje', document.getElementById('mensajeModificar').value);

  let date = $('#datetimepickerModificar').datetimepicker('getValue');
  // Formatear la fecha
  const year = date.getUTCFullYear();
  const month = String(date.getUTCMonth() + 1).padStart(2, '0'); // Los meses son de 0 a 11
  const day = String(date.getUTCDate()).padStart(2, '0');
  const hours = String(date.getUTCHours()).padStart(2, '0');
  const minutes = String(date.getUTCMinutes()).padStart(2, '0');

  const fecha_Hora = year + "/" + month + "/" + day + " " + hours + ":" + minutes;

  formData.append('fecha', fecha_Hora);

  // Si se ha seleccionado una imagen nueva, la añade al formData. 
  if (imagenSeleccionada) {
    formData.append('imagen', imagenSeleccionada, imagenSeleccionada.name);
  }

  fetch(URL + 'turnos/' + turnoId, {
    method: 'PUT',
    body: formData,
  })
    .then(response => {
      if (response.ok) {
        return response.json()
      } else {
        throw new Error('Error al guardar los cambios del turno.')
      }
    })
    .then(data => {
      alert('Turno actualizado correctamente.');
      limpiarFormulario();
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Error al actualizar el turno.');
    });
}

// Restablece todas las variables relacionadas con el formulario a sus valores iniciales, lo que efectivamente "limpia" el formulario.
function limpiarFormulario() {
  document.getElementById('nombreModificar').value = '';
  document.getElementById('apellidoModificar').value = '';
  document.getElementById('emailModificar').value = '';
  document.getElementById('telefonoModificar').value = '';
  document.getElementById('datetimepickerModificar').value = '';
  document.getElementById('mensajeModificar').value = '';

  const imagenActual = document.getElementById('imagen-actual');
  imagenActual.style.display = 'none';

  const imagenVistaPrevia = document.getElementById('imagen-vista-previa');
  imagenVistaPrevia.style.display = 'none';

  turnoId = '';
  nombre = '';
  apellido = '';
  email = '';
  telefono = '';
  mensaje = '';
  imagen_url = '';
  imagenSeleccionada = null;
  imagenUrlTemp = null;
  mostrarDatosTurno = false;

  document.getElementById('datos-turno').style.display = 'none';
}

