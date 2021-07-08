function sendUsrAge() {
    var usrAge = document.getElementById("usrAge");
    if (usrAge.value != "") {
        eel.send_usrAge(usrAge.value)(processAcknowledgement_usrAge);
        sendUsrHeight();
    } else {
        window.alert("Please enter all columns!");
    }
}

function sendUsrHeight() {
    var textbox = document.getElementById("usrHeight");
    if (textbox.value != "") {
        eel.send_usrHeight(textbox.value)(processAcknowledgement_usrHeight);
        sendUsrCurrentWeight();
    } else {
        window.alert("Please enter all columns!");
    }
}

function sendUsrCurrentWeight() {
    var textbox = document.getElementById("usrCurrentWeight");
    if (textbox.value != "") {
        eel.send_usrCurrentWeight(textbox.value)(processAcknowledgement_usrCurrentWeight);
        sendUsrIdealWeight();
    } else {
        window.alert("Please enter all columns!");
    }
}

function sendUsrIdealWeight() {
    var textbox = document.getElementById("usrIdealWeight");
    if (textbox.value != "") {
        eel.send_usrIdealWeight(textbox.value)(processAcknowledgement_usrIdealWeight);
        nextPage();
    } else {
        window.alert("Please enter all columns!");
    }
}

function nextPage() {
    window.location = "user_homepage.html";
}

function processAcknowledgement_usrAge(result) {
    if (result == "ok") {
        var textbox = document.getElementById("usrAge");
        textbox.value = "";
    }
}

function processAcknowledgement_usrHeight(result) {
    if (result == "ok") {
        var textbox = document.getElementById("usrAge");
        textbox.value = "";
    }
}

function processAcknowledgement_usrCurrentWeight(result) {
    if (result == "ok") {
        var textbox = document.getElementById("usrAge");
        textbox.value = "";
    }
}

function processAcknowledgement_usrIdealWeight(result) {
    if (result == "ok") {
        var textbox = document.getElementById("usrAge");
        textbox.value = "";
    }
}