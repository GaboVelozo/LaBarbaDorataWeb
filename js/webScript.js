// function validateForm() {
//   let cumple = true;
//   let nom = document.forms["contacto-form"]["nombre"].value;
//   if (nom == "" || nom.length < 3) {
//     document.getElementById('NombreError').hidden = false;
//     cumple = false;
//   } else document.getElementById('NombreError').hidden = true;

//   let ape = document.forms["contacto-form"]["apellido"].value;
//   if (ape == "" || ape.length < 3) {
//     document.getElementById('ApellidoError').innerHTML = "Por favor ingrese su apellido";

//     cumple = false;
//   } else document.getElementById('ApellidoError').hidden = true;

//   let email = document.forms["contacto-form"]["email"].value;
//   const regexEmail =
//     /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
//   if (email == "" || !String(email).toLowerCase().match(regexEmail)) {
//     document.getElementById('EmailError').innerHTML = "Por favor ingrese un direccion de correo electrónico válido";

//     cumple = false;
//   } else document.getElementById('EmailError').hidden = true;

//   let tel = document.forms["contacto-form"]["telefono"].value;
//   if (tel == "" || tel.length < 5) {
//     document.getElementById('TelError').innerHTML = "Por favor ingrese un teléfono válido";

//     cumple = false;
//   } else document.getElementById('TelError').hidden = true;

//   let msg = document.forms["contacto-form"]["mensaje"].value;
//   if (msg == "" || msg.length < 3) {
//     document.getElementById('MensajeError').innerHTML = "Por favor ingrese un mensaje";

//     cumple = false;
//   } else document.getElementById('MensajeError').hidden = true;

//   if (cumple) {
//     alert('Le responderemos a la brevedad! Gracias por su contacto!');
//     return false;
//   }
//   else return cumple;
// }

function loadFile(filename, elementId) {
  fetch(filename)
    .then(response => response.text())
    .then(data => document.getElementById(elementId).innerHTML = data)
    .catch(error => console.error('Error loading file:', error));
}

document.addEventListener("DOMContentLoaded", function () {
  loadFile('_header.html', 'header');
  loadFile('_footer.html', 'footer');
});
