window.addEventListener("load", function () {
    var loader = document.getElementById("loader-wrapper");
    var mainContent = document.getElementById("main-content");
    
    // Скрываем загрузочный экран
    loader.style.display = "none";
    
    // Показываем основное содержимое страницы
    mainContent.style.display = "block";
});