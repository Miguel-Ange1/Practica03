document.addEventListener("DOMContentLoaded", () => {
    // Funcionalidad para el acordeón en la página de contacto
    const itemsAcordeon = document.querySelectorAll(".item_acordeon")

    itemsAcordeon.forEach((item) => {
        const titulo = item.querySelector(".titulo_acordeon")

        titulo.addEventListener("click", () => {
            // Cerrar todos los acordeones abiertos
            itemsAcordeon.forEach((otroItem) => {
                if (otroItem !== item) {
                    otroItem.classList.remove("activo")
                }
            })

            // Alternar el estado del acordeón actual
            item.classList.toggle("activo")
        })
    })

    // Funcionalidad para mensajes flash
    const mensajesFlash = document.querySelector(".mensajes_flash")
    if (mensajesFlash) {
        setTimeout(() => {
            mensajesFlash.style.opacity = "0"
            setTimeout(() => {
                mensajesFlash.style.display = "none"
            }, 500)
        }, 5000)
    }
})
