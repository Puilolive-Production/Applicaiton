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
        sendUsrGender();
    } else {
        window.alert("Please enter all columns!");
    }
}

function sendUsrGender() {
    var textbox = document.getElementById("usrGender");
    if (textbox.value != "") {
        eel.send_usrGender(textbox.value)(processAcknowledgement_usrGender);
        sendUsrSMM();
    } else {
        window.alert("Please enter all columns!");
    }
}

function sendUsrSMM() {
    var textbox = document.getElementById("usrSMM");
    if (textbox.value != "") {
        eel.send_usrSMM(textbox.value)(processAcknowledgement_usrSMM);
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

function processAcknowledgement_usrGender(result) {
    if (result == "ok") {
        var textbox = document.getElementById("usrAge");
        textbox.value = "";
    }
}

function processAcknowledgement_usrSMM(result) {
    if (result == "ok") {
        var textbox = document.getElementById("usrAge");
        textbox.value = "";
    }
}