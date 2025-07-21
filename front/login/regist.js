function doNext() {
    document.getElementById("reg2").hidden = false;
    document.getElementById("reg1").hidden = true;
}

function checkFill() {
    if (document.getElementById("username").value == "" || document.getElementById("password1").value == "" || document.getElementById("password2").value == "" || document.getElementById("email").value == "") {
        document.getElementById("error").hidden = false;
        //console.log("baba");
    }
    else {
        doNext();
    }
}

function finCheckFill() {
    if (document.getElementById("school").value == "" || document.getElementById("grade").value == "" || document.getElementById("full_name").value == "") {
        document.getElementById("error2").hidden = false;
        console.log("baba");
    }
    else {
        console.log("yo");
        document.location.href = "../main.html";
    }
}