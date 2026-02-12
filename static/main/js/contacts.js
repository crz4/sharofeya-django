document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("tg-form");
    const telegramUsername = "Inna17Sher"; // твой Telegram username

    form.addEventListener("submit", function(e) {
        e.preventDefault(); // не перезагружаем страницу

        // получаем значения полей
        const name = document.getElementById("name").value;
        const phone = document.getElementById("phone").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        // формируем текст для Telegram
        let text = `Новая заявка с сайта ШароФея:\n`;
        text += `Имя: ${name}\n`;
        if (phone) text += `Телефон: ${phone}\n`; // добавляем только если введен
        text += `Email: ${email}\n`;
        text += `Сообщение:\n${message}`;

        // кодируем текст для URL
        const encodedText = encodeURIComponent(text);

        // формируем ссылку на Telegram
        const tgLink = `https://t.me/${telegramUsername}?text=${encodedText}`;

        // открываем Telegram в новой вкладке
        window.open(tgLink, "_blank");

        // очищаем форму
        form.reset();
    });
});
