document.getElementById("form-contacto").addEventListener("submit", function(e) {
  e.preventDefault();
  const form = e.target;
  fetch("/api/contacto", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      nombre: form.nombre.value,
      email: form.email.value,
      mensaje: form.mensaje.value
    })
  }).then(res => res.json()).then(data => {
    alert(data.mensaje || "Enviado");
  });
});