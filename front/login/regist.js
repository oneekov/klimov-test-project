function doNext() {
    document.getElementById("reg2").hidden = false;
    document.getElementById("reg1").hidden = true;
}

function checkFill() {
    if (document.getElementById("username").value == "" || document.getElementById("password1") == "" || document.getElementById("password2") == "" || document.getElementById("email") == "") {
        document.getElementById("error").hidden = false;
        //console.log("baba");
    }
    else {
        doNext();
    }
}

function finCheckFill() {
    if (document.getElementById("school").value == "" || document.getElementById("grade") == "" || document.getElementById("full_name") == "") {
        document.getElementById("error2").hidden = false;
        //console.log("baba");
    }
    else {
        document.location.href = "../main.html";
    }
}