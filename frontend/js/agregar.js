document.getElementById("form-agregar").addEventListener("submit", function(e) {
  e.preventDefault();
  const form = e.target;

  const producto = {
    marca: form.marca.value,
    nombre: form.nombre.value,
    precio: parseFloat(form.precio.value),
    modelo: form.modelo.value,
    stock: parseInt(form.stock.value)
  };

  fetch("/api/productos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(producto)
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("mensaje").innerText = data.message || "Producto agregado.";
    form.reset();
  })
  .catch(err => {
    document.getElementById("mensaje").innerText = "Error al guardar el producto.";
    console.error(err);
  });
});