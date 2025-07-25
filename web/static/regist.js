function doNext() {
    if (document.getElementById("password1").value == document.getElementById("password2").value) {
        document.getElementById("reg2").hidden = false;
        document.getElementById("reg1").hidden = true;
    }
    else {
        document.getElementById("error").textContent = "Пароли не совпадают";
        document.getElementById("error").hidden = false;
    }
}

function checkFill() {
    if (document.getElementById("username").value == "" || document.getElementById("password1").value == "" || document.getElementById("password2").value == "") {
        document.getElementById("error").textContent = "Пожалуйста повторите ввод";
        document.getElementById("error").hidden = false;
    }
    else {
        console.log("1 form ok");
        doNext();
    }
}

function finCheckFill() {
    if (document.getElementById("school").value == "" || document.getElementById("grade").value == "" || document.getElementById("full_name").value == "") {
        document.getElementById("error2").hidden = false;
        console.log("baba");
    }
    else {
        sendInfo()
        //submitForms();
        console.log("yo");
    }
}

async function sendInfo() {
    try {
        // Collect data from first form
        const authData = {
            username: document.getElementById('username').value,
            password: document.getElementById('password1').value,
            email: document.getElementById('email').value
        };

        // Collect data from second form
        const nameParts = document.getElementById('full_name').value.trim().split(/\s+/);
        const profileData = {
            school: document.getElementById('school').value,
            grade: [parseInt(document.getElementById('grade').value), "A"],
            full_name: nameParts.length > 0 ? nameParts : ["", ""] // Ensure we have at least two elements
        };

        // Combine data
        const combinedData = { ...authData, ...profileData };

        // Send POST request
        const response = await fetch('/api/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(combinedData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.message || `HTTP error: ${response.status}`);
        }

        const result = await response.json();
        console.log("Registration successful:", result);

        // Сохраняем токен в куки (на 1 день)
        if (result.token) {
            createCookie('auth_token', result.token, 1);
        }

        document.location.href = "/test";

    } catch (error) {
        console.error('Error:', error);
        document.getElementById("error2").textContent = error.message || "Registration failed";
        document.getElementById("error2").hidden = false;
        throw error; // Re-throw so finCheckFill can handle it
    }
}

function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}
window.addEventListener('DOMContentLoaded', function() {
    const token = getCookie('auth_token');
    if (token !== "") {
        window.location.href = '/test';
    }
});
