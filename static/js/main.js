setTimeout(function() {
    let messages = document.querySelector('.messages-container');
    if (messages) {
        messages.style.transition = "opacity 0.5s ease";
        messages.style.opacity = "0";
        setTimeout(() => messages.remove(), 500);
    }
}, 5000);