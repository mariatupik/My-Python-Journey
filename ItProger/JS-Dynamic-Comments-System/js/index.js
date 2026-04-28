let btnForm = document.querySelector("#comments-form button");
let countComments = 0;
let idComment = 0;

btnForm.onclick = () => {
    let form = document.getElementById("comments-form");
    let error = document.querySelector("#error");

    idComment++;
    if (form.username.value.length < 2) {
        error.innerText = "Довжина імені не може бути менше 2 символа";
        return false;
    } else if (form.comment.value.length < 10) {
        error.innerText = "Довжина коментаря не може бути менше 10 символів";
        return false;
    }

    error.innerText = '';

    // Встановимо нове значення для підрахунку коментарів
    if (countComments == 0)
        document.querySelector("#comments").innerHTML = "";

    countComments++;
    document.querySelector("#count-comm").innerText = countComments;

    let newComment = "<div class='comment' id='block-" + idComment + "'>" +
        "<span class='delete' onclick='delComm(" + idComment + ")'>&times;</span>" +
        "<p class='name'>" + form.username.value + "</p>" +
        "<p class='mess'>" + form.comment.value + "</p>" +
        "</div>";

    document.querySelector('#comments').insertAdjacentHTML('afterbegin', newComment);

    // Clear form
    form.comment.value = '';
}

function delComm(id) {
    document.querySelector("#block-" + id).remove();

    countComments--;
    document.querySelector("#count-comm").innerText = countComments;

    if (countComments == 0)
        document.querySelector("#comments").innerHTML = "Поки що немає коментарів";
}
