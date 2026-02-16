document.addEventListener('DOMContentLoaded', () => {
    // =============================
    // Добавление товаров в корзину
    // =============================
    const buttons = document.querySelectorAll('.add-to-cart');
    const notif = document.getElementById('cart-notification');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const productId = btn.getAttribute('data-id');
            const url = btn.getAttribute('data-url');

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: `product_id=${productId}`
            })
            .then(response => {
                // проверяем, что сервер вернул JSON
                if (!response.ok) throw new Error('Сервер вернул ошибку!');
                return response.json();
            })
            .then(data => {
                if (data.success && notif) {
                    notif.style.display = 'block';
                    setTimeout(() => { notif.style.display = 'none'; }, 2000);
                }
            })
            .catch(error => {
                console.error('Ошибка AJAX:', error);
                // alert('Ошибка добавления товара!'); // убираем alert, чтобы не мешало UX
            });
        });
    });

    // =============================
    // Авто-добавление +7 к номеру
    // =============================
    const phoneInput = document.getElementById('phone');
    if (phoneInput) {
        phoneInput.addEventListener('input', () => {
            let val = phoneInput.value.replace(/\D/g, '');
            if (!val.startsWith('7')) val = '7' + val;
            phoneInput.value = '+' + val;
        });
    }

    // =============================
    // Функция получения CSRF-токена
    // =============================
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
