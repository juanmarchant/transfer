


document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#form')

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        console.log('Enviado Formulario')

        setTimeout(() => {
            form.submit()
        }, 3000);
    })
})




