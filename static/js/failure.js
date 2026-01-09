document.addEventListener('DOMContentLoaded', () => {
    const card = document.getElementById('card');
    setTimeout(() => {
        card.classList.add('active');
        card.classList.add('visible');
    }, 150);
});