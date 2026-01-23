document.querySelectorAll('.review-card img').forEach(img => {
    img.addEventListener('click', () => {
        const modal = document.getElementById('review-modal');
        const modalImg = document.getElementById('review-modal-img');

        modal.style.display = 'flex';
        modalImg.src = img.src;
    });
});

document.querySelector('.modal .close').addEventListener('click', () => {
    document.getElementById('review-modal').style.display = 'none';
});
