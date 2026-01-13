/* ===== ФИЛЬТРАЦИЯ ГАЛЕРЕИ ===== */
const galleryItems = document.querySelectorAll(".gallery-item");
const showAllBtn = document.querySelector(".show-all");

galleryItems.forEach(item => {
    item.addEventListener("click", (e) => {
        const category = item.dataset.category;

        galleryItems.forEach(el => {
            if (el.dataset.category === category) {
                el.style.display = "block";
            } else {
                el.style.display = "none";
            }
        });
    });
});

if (showAllBtn) {
    showAllBtn.addEventListener("click", () => {
        galleryItems.forEach(item => item.style.display = "block");
    });
}

/* ===== МОДАЛЬНОЕ ОКНО ОТЗЫВОВ ===== */
const reviewModal = document.getElementById("review-modal");
const modalImg = document.getElementById("review-modal-img");
const closeBtn = reviewModal.querySelector(".close");
const reviewCards = document.querySelectorAll(".review-card img");

reviewCards.forEach(img => {
    img.addEventListener("click", () => {
        reviewModal.style.display = "flex";
        modalImg.src = img.src;
    });
});

closeBtn.addEventListener("click", () => {
    reviewModal.style.display = "none";
});

reviewModal.addEventListener("click", (e) => {
    if (e.target === reviewModal) reviewModal.style.display = "none";
});


