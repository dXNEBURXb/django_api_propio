document.getElementById("logout-link").addEventListener("click", function (event) {
    event.preventDefault(); // Previene la acción predeterminada del enlace

    Swal.fire({
      title: '¿Estás seguro?',
      text: "Perderas tu sesion actual.",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Sí, cerrar sesión',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = '/logout/'; // Redirige al logout si se confirma
      }
    });
  });