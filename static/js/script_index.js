const button = document.querySelector('#buttonLOGO');

button.addEventListener('click', () => {
    open('/', '_self');
})
button.addEventListener('contextmenu', (e) => {
    e.preventDefault();
})