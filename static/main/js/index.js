/* ===== ФИЛЬТРАЦИЯ ГАЛЕРЕИ ===== */
const galleryItems = document.querySelectorAll(".gallery-item");
const showAllBtn = document.querySelector(".show-all");

/* ВСЕГДА показываем все элементы при загрузке и возврате */
window.addEventListener("pageshow", () => {
    galleryItems.forEach(item => {
        item.style.display = "block";
    });
});

if (galleryItems.length > 0) {
    galleryItems.forEach(item => {
        item.addEventListener("click", () => {
            const category = item.dataset.category;

            galleryItems.forEach(el => {
                el.style.display =
                    el.dataset.category === category ? "block" : "none";
            });
        });
    });
}

if (showAllBtn) {
    showAllBtn.addEventListener("click", () => {
        galleryItems.forEach(item => item.style.display = "block");
    });
}

/* ===== МОДАЛЬНОЕ ОКНО ОТЗЫВОВ ===== */
const reviewModal = document.getElementById("review-modal");
const modalImg = document.getElementById("review-modal-img");
const closeBtn = reviewModal?.querySelector(".close");
const reviewCards = document.querySelectorAll(".review-card img");

if (reviewModal && reviewCards.length > 0) {

    reviewModal.style.display = "none";

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
        if (e.target === reviewModal) {
            reviewModal.style.display = "none";
        }
    });
}
