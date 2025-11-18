const button = document.querySelector('#buttonLOGO');

button.addEventListener('click', () => {
    open('/', '_self');
})

button.addEventListener('conextmenu', (e) => {
    e.preventDefault();
})