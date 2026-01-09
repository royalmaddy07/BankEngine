document.addEventListener('DOMContentLoaded', () => {
    const card = document.getElementById('card');
    const iconBox = document.getElementById('iconBox');
    const title = document.getElementById('title');
    const subtitle = document.getElementById('subtitle');

    setTimeout(() => {
        card.classList.add('active');
        card.classList.add('visible');
    }, 150);

    setTimeout(() => {
        confetti({
            particleCount: 150,
            spread: 60,
            origin: { y: 0.7 },
            colors: ['#10b981', '#1e293b', '#ffffff']
        });

        iconBox.classList.remove('loading');
        iconBox.classList.add('success');

        title.innerText = "Payment Successful!";
        subtitle.innerText = "Your funds have been transferred successfully.";

        card.style.transform = 'scale(1.02)';
        setTimeout(() => card.style.transform = 'scale(1)', 200);
    }, 2200);
});