function cargarProductos() {
  fetch("http://localhost:5000/api/productos")
    .then((res) => res.json())
    .then((productos) => {
      const contenedor = document.getElementById("lista-productos");
      productos.forEach((p) => {
        const li = document.createElement("li");
        li.textContent = `${p.nombre} (${p.marca}) - $${p.precio}`;
        contenedor.appendChild(li);
      });
    });
}