document.addEventListener("DOMContentLoaded", function() {
    const input = document.getElementById("search-input");
    const box = document.getElementById("suggestions-box");

    if (!input) return;

    input.addEventListener("input", function() {
        let query = this.value;

        if (query.length < 2) {
            box.style.display = "none";
            return;
        }

        fetch(`/goods/search/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                box.innerHTML = "";

                if (data.results.length > 0) {
                    box.style.display = "block";

                    data.results.forEach(item => {
                        let div = document.createElement("div");
                        div.classList.add("suggestion-item");
                        div.innerText = item.title;

                        div.onclick = () => {
                            input.value = item.title;
                            box.style.display = "none";
                        };

                        box.appendChild(div);
                    });
                } else {
                    box.style.display = "none";
                }
            });
    });

    document.addEventListener("click", function(e) {
        if (!e.target.closest(".filter-group")) {
            box.style.display = "none";
        }
    });
});
