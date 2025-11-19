const goToIndex = document.querySelector('#backIndex');
const goToGame = document.querySelector('#backGame');

goToIndex.addEventListener('click', () => {
    open('/', '_self');
});

goToGame.addEventListener('click', () => {
    open('/game', '_self');
});

goToIndex.addEventListener('contextmenu', (e) => {
    e.preventDefault();
});

goToGame.addEventListener('contextmenu', (e) => {
    e.preventDefault();
});