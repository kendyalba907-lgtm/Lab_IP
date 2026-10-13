async function cargarConfiguracion() {
    const respouesta=await fetch("/api/config");

    if (!respuesta.ok) {
        throw new Error("No se pudo cargar ");
    }

    const datos=await respuesta.json();
    document.querySelector("#titulo").textContent=datos.titulo;
}

cargarConfiguracion(); 