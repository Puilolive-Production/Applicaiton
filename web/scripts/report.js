currentusrCurrentWeight = 0.0
currentusrHeight = 0.0
currentusrAge = ""
currentusrGender = ""
currentusrSMM = 0.0
bmi = 0.0
bmr = 0.0
tdee = 0.0
smm - 0.0
bfp = 0.0

function getcurrentUsrinfo() {
    eel.send_currentUsrinfo()(processAcknowledgement_currentUsrname);
}

function processAcknowledgement_currentUsrname(currentusrInfo_Arr) {
    currentusrAge = currentusrInfo_Arr[0];
    console.log("currentusrAge: ", currentusrAge);

    currentusrHeight = currentusrInfo_Arr[1];
    console.log("currentusrHeight: ", currentusrHeight);
    document.getElementById('currentusrHeight').innerHTML = currentusrHeight;
    currentusrHeight = currentusrHeight / 100;

    currentusrCurrentWeight = currentusrInfo_Arr[2];
    console.log("currentusrCurrentWeight: ", currentusrCurrentWeight);
    document.getElementById('currentusrCurrentWeight').innerHTML = currentusrCurrentWeight;

    currentusrGender = currentusrInfo_Arr[3];
    console.log("currentusrGender: ", currentusrGender);
    console.log("currentusrGender: ", currentusrGender.toLowerCase());

    currentusrSMM = currentusrInfo_Arr[4];
    console.log("currentusrSMM: ", currentusrSMM);

    bmi = currentusrCurrentWeight / (currentusrHeight * currentusrHeight);
    console.log("bmi: ", bmi);
    document.getElementById('bmi').innerHTML = bmi.toFixed(0);

    bmr = 1216;

    if (currentusrGender.toLowerCase() == "male") {
        bmr = 66 + (13.7 * currentusrCurrentWeight) + (5 * currentusrHeight) - (6.8 * currentusrAge);
        console.log("bmr: ", bmr);
    } else if (currentusrGender.toLowerCase() == "female") {
        bmr = 655 + (9.6 * currentusrCurrentWeight) + (1.8 * currentusrHeight) - (4.7 * currentusrAge);
        console.log("bmr: ", bmr);
    }
    tdee = bmr * 1.55;
    console.log("tdee: ", tdee);
    document.getElementById('tdee').innerHTML = tdee.toFixed(0);

    smm = (currentusrSMM / currentusrCurrentWeight) * 100;
    console.log("smm: ", smm);
    document.getElementById('smm').innerHTML = smm.toFixed(0);

    if (currentusrGender.toLowerCase() == "male") {
        bfp = 1.2 * bmi + 0.23 * currentusrAge - 5.4 - 10.8 * 1
        console.log("bfp: ", bfp);
        document.getElementById('bfp').innerHTML = bfp.toFixed(0);
    } else if (currentusrGender.toLowerCase() == "female") {
        bfp = 1.2 * bmi + 0.23 * currentusrAge - 5.4 - 10.8 * 0
        console.log("bfp: ", bbfpmr);
        document.getElementById('bfp').innerHTML = bfp.toFixed(0);
    }
}