const targetNumber = 8;
function askNumber() {
    const userInput = prompt("Введіть число:");

    if (userInput === null) {
        console.log("Введення скасовано користувачем.");
        return;
    }

    if (Number(userInput) !== targetNumber) {
        console.log("Ви ввели неправильне число! Спробуйте ще раз.");
        setTimeout(askNumber, 10); 
    } else {
        console.log("Вітаємо! Ви ввели правильне число: 8.");
        window.focus();
    }
}

function updateSize() {
    const dimensionsText = document.getElementById('dimensions');
    if (dimensionsText) {
        dimensionsText.textContent = `Ширина - ${window.innerWidth}; висота - ${window.innerHeight}`;
    }
}

function getAttributes(e) {
    if (e && e.preventDefault) e.preventDefault();

    const link = document.getElementById('link');
    if (!link) return;

    console.log("Атрибути посилання:");
    console.log("href: " + link.getAttribute('href'));
    console.log("hreflang: " + link.getAttribute('hreflang'));
    console.log("rel: " + link.getAttribute('rel'));
    console.log("target: " + link.getAttribute('target'));
    console.log("type: " + link.getAttribute('type'));
}

function setupBoldWords() {
    const paragraph = document.getElementById('main-paragraph');
    if (!paragraph) return;

    const boldWords = paragraph.getElementsByTagName('b');

    paragraph.onmouseenter = function() {
        for (let i = 0; i < boldWords.length; i++) {
            boldWords[i].style.color = 'red';
        }
    };

    paragraph.onmouseleave = function() {
        for (let i = 0; i < boldWords.length; i++) {
            boldWords[i].style.color = 'black';
        }
    };
}

document.addEventListener('DOMContentLoaded', () => {
    updateSize();      
    setupBoldWords();  
    setTimeout(askNumber, 100);
});

window.addEventListener('resize', updateSize);