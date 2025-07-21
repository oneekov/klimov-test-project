function doNext() {
    document.getElementById("reg2").hidden = false;
    document.getElementById("reg1").hidden = true;
}

function checkFill() {
    if (document.getElementById("username").value == "" || document.getElementById("password1").value == "" || document.getElementById("password2").value == "" || document.getElementById("email").value == "") {
        document.getElementById("error").hidden = false;
        console.log("baba");
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
        window.location.href = "../main.html";

    } catch (error) {
        console.error('Error:', error);
        document.getElementById("error2").textContent = error.message || "Registration failed";
        document.getElementById("error2").hidden = false;
        throw error; // Re-throw so finCheckFill can handle it
    }
}