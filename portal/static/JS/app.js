var input = document.getElementsByClassName("Formulario_input");
for ( var i = 0; i < input.length; i++) {
    input[ i ] .addEventListener("keyup" , function(){
 if(this.value.length>=1) {
    this.nextElementSibling.classList.add("fijar");
 } else {
    this.nextElementSibling.classList.remove("fijar");
 }
    });
}
 
function validar (){
   var Name, LastName, EmailDeContacto, Asunto, Comentario, expresion;
   Name = document.getElementById("Name").value;
   LastName = document.getElementById("LastName").value;
   Asunto = document.getElementById("Asunto").value;
   EmailDeContacto = document.getElementById("EmailDeContacto").value;
   Comentario = document.getElementById("Comentario").value;
   expresion = /\w+@\w+\.+[a-z]/;
 
   if(Name === "" || LastName === "" || EmailDeContacto === "" || Asunto === "" || Comentario === ""){
      alert("Todos los campos son obligatorios");
      return false;
   }
   else if(Name.length>30) {
      alert("El Nombre debe tener menos de 30 caracteres");
      return false;
   }
   else if(LastName.length>80) {
      alert("El Apellido debe tener menos de 80 caracteres");
      return false;
   }
   else if(EmailDeContacto.length>100) {
      alert("El Email es muy largo");
      return false;
   }
   else if(!expresion.test(EmailDeContacto)){
      alert("El Email no es válido");
      return false;
   }
   else if(Asunto.length>100) {
      alert("El Asunto es muy largo");
      return false;
   }
   else if(Comentario.length>1500) {
      alert("El mensaje no puede tener más de 1500 caracteres");
      return false;
   }
}

const $form = document.querySelector('#form')
$form.addEventListener('submit', handleSubmit)

async function handleSubmit(event) {
  event.preventDefault()
  const form = new FormData(this)
  const response = await fetch(this.action, {
    method: this.method,
    body:form,
    headers:{
      'Accept': 'application/json'      }
  })

  if(response.ok){
    this.reset()
    swal("Muchas Gracias!", "Tu mensaje ha sido enviado. Te responderemos a la brevedad", "success");
    
  }
}